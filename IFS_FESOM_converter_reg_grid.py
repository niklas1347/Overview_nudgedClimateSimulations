import numpy as np
import xarray as xr
import glob
import os
from pyresample import geometry, kd_tree

# =========================
# FIND FILES
# =========================
files = sorted(glob.glob(input_pattern))
print(f"Found {len(files)} files")

# extract first and last timestamps from filenames
first_file = os.path.basename(files[0])
last_file = os.path.basename(files[-1])

first_tag = first_file.split("_")[-1].replace(".nc", "")
last_tag = last_file.split("_")[-1].replace(".nc", "")

# =========================
# USER SETTINGS
# =========================
#Change the param
param_str = "167"

input_pattern = f"/work/bb1445/b383514/data/ifs-fesmo/api/hist/{param_str}/{realisation}/{param_str}_ifs-fesom_hist_*.nc"
output_path = f"/work/bb1445/b383514/data/ifs-fesmo/api/hist/{param_str}/{param_str}_ifs-fesom_hist_{realisation}_{first_tag}_{last_tag}.nc"
realisation = "E5"

# =========================
# DEFINE TARGET GRID (HIGH RES)
# =========================
lat_reg = np.linspace(-90, 90, 1801)
lon_reg = np.linspace(-179.9, 179.9, 1800)

lon_grid, lat_grid = np.meshgrid(lon_reg, lat_reg)
target_def = geometry.GridDefinition(lons=lon_grid, lats=lat_grid)

# =========================
# PROCESS FILES
# =========================
all_datasets = []

for f in files:
    print(f"\nProcessing file: {f}")

    ds = xr.open_dataset(f)

    lat = ds["latitude"].values
    lon = ds["longitude"].values
    lon = (lon + 180) % 360 - 180

    # geometry
    orig_def = geometry.SwathDefinition(lons=lon, lats=lat)

    # output container for this file
    ds_out_vars = {}

    # =========================
    # LOOP OVER VARIABLES
    # =========================
    for var_name, da_in in ds.data_vars.items():
        print(f"  Variable: {var_name}")

        data = da_in.values  # (time, points)

        resampled_list = []

        for t in range(data.shape[0]):
            print(f"    timestep {t+1}/{data.shape[0]}")

            field = data[t, :]

            resampled = kd_tree.resample_gauss(
                orig_def,
                field,
                target_def,
                radius_of_influence=12000,
                sigmas=6000,
                fill_value=np.nan
            )

            da = xr.DataArray(
                resampled,
                dims=("lat", "lon"),
                coords={"lat": lat_reg, "lon": lon_reg}
            )

            resampled_list.append(da)

        # combine time for this variable
        da_out = xr.concat(resampled_list, dim="forecast_reference_time")
        da_out["forecast_reference_time"] = ds["forecast_reference_time"]

        ds_out_vars[var_name] = da_out

    # =========================
    # COMBINE VARIABLES
    # =========================
    ds_out = xr.Dataset(ds_out_vars)

    all_datasets.append(ds_out)

# =========================
# COMBINE ALL FILES
# =========================
final_dataset = xr.concat(all_datasets, dim="forecast_reference_time")
final_dataset = final_dataset.rename({"forecast_reference_time": "time"})

# =========================
# SAVE OUTPUT
# =========================
os.makedirs(os.path.dirname(output_path), exist_ok=True)
final_dataset.to_netcdf(output_path)

print("Saved to:", output_path)