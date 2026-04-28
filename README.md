# Overview_nudgedClimateSimulations
This repository provides an overview of available wind‑nudged climate model simulations. It includes general descriptions of the datasets, along with guidance on how to access and use the data.

## 🌟 General information about nudged climate storyline simulations

Nudged model simulations refer to a class of climate experiments in which key aspects of the large-scale atmospheric circulation — most commonly winds — are constrained toward observational or reanalysis data during the simulation, while the model is otherwise free to generate its own small-scale processes and internal variability. This approach ensures consistency with the observed large-scale evolution while retaining a physically coherent representation of regional dynamics and feedbacks.

Within the climate storyline framework, nudged simulations are used to isolate and examine the thermodynamic response of the climate system under different conditions by replaying specific events in alternative climates ("storylines"). By reducing variability associated with circulation differences, they provide a controlled setting for investigating how factors such as temperature, moisture, or external forcings influence impacts.

The conceptual basis of this approach is discussed in [Shepherd (2016)](https://doi.org/10.1007/s40641-016-0033-y), which outlines a general framework for event-based climate analysis, and further developed for nudged storyline applications in [Feser & Shepherd (2025)](https://doi.org/10.1038/s43247-025-02659-6).

## 🛠 Included climate models in this overview

| Model | Type | Spatial Resolution | Nuding Method | Nuding dataset | SST | Experiments | Time period | Ensemble members | Data archive |
| ------------- |-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| CESM2 | fully-coupled | 0.9° lat x 1.25° lon | grid-point nudging | ERA5 | prescribed | HIST <br> NAT | 1940‑2024 <br> 1940‑2024 | 1 <br> 1 | DKRZ |
| IFS-FESOM | fully-coupled | 0.1° lat x 0.2° lon | spectral nudging | ERA5 | free | HIST <br> NAT | 2017‑2024 <br> 2017‑2024 | 1 <br> 1 | DestinE/DKRZ |
| AWI-CM-1 | fully-coupled | T127 <br> ~0.94° lat x ~0.94° lon | spectral nudging | ERA5 | free | HIST <br> NAT | 2014‑2025 <br> 2014‑2025 | 5 <br> 5 | DKRZ |
| ECHAM6 | atmospheric circulation only | T255 <br> ~0.47° lat x ~0.47° lon | spectral nudging | NCEP-NCAR-1 | prescribed | HIST <br> NAT | 2015‑present <br> 2015‑present | 5 <br> 5 | DKRZ |

## CESM2
In summary, atmospheric grid-point nudging to ERA5 meridional and zonal winds was applied down to 700 hPa using a standard relaxation procedure at 3‑hourly intervals, while allowing the planetary boundary layer to evolve freely. In addition, sea surface temperatures were prescribed to observed and counterfactual values to ensure a physically plausible representation in the climate model. Counterfactual SSTs were estimated using a pattern filtering method [Wills et al. (2020)](https://doi.org/10.1175/JCLI-D-19-0855.1). NUDGING TIME???

#### Data ownership:
The simulations are created by the research group of Prof. Sebastian Sippel at the University of Leipzig. Contact with the working group is mandatory before usage of the data. Contact persons are [Sebastian Sipple](mailto:sebastian.sippel@uni-leipzig.de) or [István Dunkl](mailto:istvan.dunkl@uni-leipzig.de).

#### Key literature:
* [Pfleiderer et al. (2025)](https://doi.org/10.5194/wcd-7-89-2026)

#### Available simulations:
| Simulation | Appreviation | Description | Covered timeperiod | Ensemble members |
| ------------- |-------------|-------------|-------------|-------------|
| Historical | HIST | historical CO2 | 1940‑2024 | 1 |
| Pre-industrial | NAT | 1850 CO2 (282ppm) and aerosol levels | 1940‑2024 | 1 |
|  | THERM | Historical without CO2 fertilization | 1940‑2024 | 1 |
|  | PD | Costant present-day forcing | 1940‑2024 | 1 |

#### Overview of the available variables:

A variety of different atmospheric and land related variabels are saved at daily and monthly time scales. A full overview is provided in the Juptyer Notebook: [Load_nudging_CESM2.ipynb](Load_nudging_CESM2.ipynb)

#### Access the data:

A DKRZ account is mandatory to access the data. A detailed description of how to download the data is provided in the Jupyter Notebook: [Load_nudging_CESM2.ipynb](Load_nudging_CESM2.ipynb)

## IFS-FESOM
In short, Newtonian relaxation spectral nudging to ERA5 is applied to vorticity and divergence between 100 and 700 hPa, with a sigmoidal transition. This allows the planetary boundary layer and air-sea-ice coupling to develop freely. A triangular truncation of T60 with a relatively short relaxation time timescale (e-folding time) of 1 hour is used for the nudging.

#### Data ownership:
This simulations forms a core operational component of the EU’s Destination Earth Climate Digital Twin, enabling scalable, high-resolution, circulation-constrained climate storylines for science and decision-making. Therefore the usage of this data is restricted according to the details outlined at the [DestinE Platform](https://platform.destine.eu).

#### Key literature:
* [John et al. (2026)](https://doi.org/10.22541/essoar.173160166.64258929/v3)

* #### Available simulations:
