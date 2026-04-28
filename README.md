# Overview_nudgedClimateSimulations
This repository provides an overview of available wind‑nudged climate model simulations. It includes general descriptions of the datasets, along with guidance on how to access and use the data.

## 🌟 General information about nudged climate storyline simulations

Nudged model simulations refer to a class of climate experiments in which key aspects of the large-scale atmospheric circulation — most commonly winds — are constrained toward observational or reanalysis data during the simulation, while the model is otherwise free to generate its own small-scale processes and internal variability. This approach ensures consistency with the observed large-scale evolution while retaining a physically coherent representation of regional dynamics and feedbacks.

Within the climate storyline framework, nudged simulations are used to isolate and examine the thermodynamic response of the climate system under different conditions by replaying specific events in alternative climates ("storylines"). By reducing variability associated with circulation differences, they provide a controlled setting for investigating how factors such as temperature, moisture, or external forcings influence impacts.

The conceptual basis of this approach is discussed in [Shepherd (2016)](https://doi.org/10.1007/s40641-016-0033-y), which outlines a general framework for event-based climate analysis, and further developed for nudged storyline applications in [Feser & Shepherd (2025)](https://doi.org/10.1038/s43247-025-02659-6).

## 🛠 Included climate models

| Model | Type | Spatial Resolution | Nuding Method | Nuding dataset | SST | Experiments | Time period | Ensemble members | Data archive |
| ------------- |-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| CESM2 | fully-coupled | 0.9° lat x 1.25° lon | grid-point nudging | ERA5 | Prescribed | HIST <br> NAT | 1940‑2024 <br> 1940‑2024 | 1 <br> 1 | DKRZ |
| IFS-FESOM | fully-coupled | 0.9° lat x 1.25° lon | grid-point nudging | ERA5 | Prescribed | HIST <br> NAT | 1940‑2024 <br> 1940‑2024 | 1 <br> 1 | DKRZ |

## CESM2
In summary, atmospheric grid-point nudging to ERA5 meridional and zonal winds was applied down to 700 hPa using a standard relaxation procedure at 3‑hourly intervals, while allowing the planetary boundary layer to evolve freely. In addition, sea surface temperatures were prescribed to observed and counterfactual values to ensure a physically plausible representation in the climate model. Counterfactual SSTs were estimated using a pattern filtering method [Wills et al. (2020)](https://doi.org/10.1175/JCLI-D-19-0855.1).

#### Data ownership:
The simulations are created by Prof. Sebastian Sippel group at the University of Leipzig. Contact with the working group is mandatory before usage of the data. Contact persons are [Sebastian Sipple](mailto:sebastian.sippel@uni-leipzig.de) or [István Dunkl](mailto:istvan.dunkl@uni-leipzig.de).

#### Key literature:
* [Pfleiderer et al. (2025)](https://doi.org/10.5194/wcd-7-89-2026)

#### Further simulations:
| Simulation | Appreviation | Description | Covered timeperiod | Ensemble members |
| ------------- |-------------|-------------|-------------|-------------|
| Historical | HIST | historical CO2 | 1940‑2024 | 1 |
| Counterfactual <br> (Pre-industrial) | NAT | 1850 CO2 (282ppm) and aerosol levels | 1940‑2024 | 1 |
| Counterfactual | THERM | Historical without CO2 fertilization | 1940‑2024 | 1 |
| Counterfactual | PD | Costant present-day forcing | 1940‑2024 | 1 |

#### Overview of the available variables:

A variety of different atmospheric and land related variabels are saved at daily and monthly time scales. A full overview is provided in the Juptyer Notebook: [Load_nudging_CESM2.ipynb](Load_nudging_CESM2.ipynb)

#### Access the data:

A DKRZ account is mandatory to access the data. A detailed description of how to download the data is provided in the Jupyter Notebook: [Load_nudging_CESM2.ipynb](Load_nudging_CESM2.ipynb)
