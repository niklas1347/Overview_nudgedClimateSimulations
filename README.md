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
| CESM3 | in preparation |  |  |  |  |  |  |  |  |
| AWI-CM-3 | in preparation |  |  |  |  |  |  |  |  |
| ICON | in preparation |  |  |  |  |  |  |  |  |

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
This simulations forms a core operational component of the EU’s Destination Earth Climate Digital Twin, enabling scalable, high-resolution, circulation-constrained climate storylines for science and decision-making. Therefore the usage of this data is restricted according to the details outlined at the [DestinE Platform](https://platform.destine.eu/support-pages/access-policy/). Contact person is [Amal John](mailto:amal.john@awi.de). 

#### Key literature:
* [John et al. (2026)](https://doi.org/10.22541/essoar.173160166.64258929/v3)

#### Available simulations:
| Simulation | Appreviation | Description | Covered timeperiod | Ensemble members |
| ------------- |-------------|-------------|-------------|-------------|
| Historical | Hist | 1950 boundary conditions | 2017‑2024 | 1 |
| Pre-industrial | Cont | recorded boundary conditions | 2017‑2024 | 1 |
|  | Tp2K | boundary conditions from a 2K warmer world | 2017‑2024 | 1 |

more deteails about the simulations can be found here:

<img width="871" height="308" alt="image" src="https://github.com/user-attachments/assets/3ed0bf0e-06c5-472e-8fa3-ba78b2ce4d59" />
Source: [John et al. (2026)](https://doi.org/10.22541/essoar.173160166.64258929/v3)

#### Overview of the available variables:
A variety of different atmospheric and ocean related variabels are saved at hourly and daily time scales. A full overview is provided on page 35ff. in [DestinE_Framework](DestinE_Framework.pdf).

#### Access the data:
To access the data it is mandatory to have an upgraded account at the [DestinE Platform](https://platform.destine.eu/support-pages/access-policy/). The data can be downloaded via the Destination Earth Polytope API as descriped in this [repository](https://github.com/John-Amal/retriever_polytop/tree/main).

## AWI-CM-1
Briefly, spectral nudging was applied to vorticity and divergence fields between 100 and 700 hPa with a sigmoidal transition, using a relaxation timescale of 24 hours and a spectral truncation at zonal wavenumber 20. Since the model is fully coupled, ocean and sea ice states are fully dynamic and can adapt to varying background climate conditions and the imposed wind anomalies.

#### Data ownership:
The simulations are created by the Alfred Wegener Institute, Helmholtz-Center for Polar and Marine Research, Bremerhaven, Germany. Contact with the working group is mandatory before usage of the data. Contact persons are [Helge Goessling](mailto:helge.goessling@awi.de), [Antonio Sánchez Benítez](mailto:antonio.sanchez.benitez@awi.de) and [Marylou Athanase](mailto:marylou.athanase@awi.de).

#### Key literature:
* [Athanase et al. (2024)](https://doi.org/10.1038/s43247-024-01847-0)
* [Sánchez-Benítez et al. (2022)](https://doi.org/10.1175/JCLI-D-21-0573.1)

#### Available simulations:
| Simulation | Appreviation | Description | Covered timeperiod | Ensemble members |
| ------------- |-------------|-------------|-------------|-------------|
| Weak Nudging |  |  |  |  |
| Historical | Hist | 1950 boundary conditions | 2017‑2024 | 1 |
| Pre-industrial | Cont | recorded boundary conditions | 2017‑2024 | 1 |
| Long-Nudged | Cont | recorded boundary conditions | 2017‑2024 | 1 |
|  | Tp2K | boundary conditions from a 2K warmer world | 2017‑2024 | 1 |
| Strong Nudging |  |  |  |  |
| Historical | Hist | 1950 boundary conditions | 2017‑2024 | 1 |
| Pre-industrial | Cont | recorded boundary conditions | 2017‑2024 | 1 |
|  | Tp2K | boundary conditions from a 2K warmer world | 2017‑2024 | 1 |

Note: The long-nudged run should not be taken as sixth ensemble member without rigorous testing.

#### Overview of the available variables:
A variety of different atmospheric and ocean related variabels are saved at hourly and daily time scales. A full overview is provided at ??.

#### Access the data:
A DKRZ account is mandatory to access the data. A detailed description of how to download the data is provided in the Jupyter Notebook: [XX](XX).

## ECHAM6
In contrast to the other three models, ECHAM6 is an atmospheric general circulation model (the atmospheric component of MPI-ESM at T255 using 95 levels) coupled to the land surface and vegetation model JSBACH. All simulations apply spectral nudging towards NCEP-NCAR Reanalysis 1 to constrain large-scale circulation patterns. Vorticity and divergence are nudged at large spatial scales above the 750 hPa level up to 3 hPa following a plateau-shaped profile with a relaxation time of 50 minutes, with no nudging applied near the surface to allow the model to freely develop regional-scale processes. The targeted warming levels are achieved by defining sea surface temperature warming or cooling patterns and greenhouse gas concentrations that correspond to the desired global‑warming magnitude. The SST warming or cooling patterns are created by adding or subtracting a climatological pattern (based on ECHAM6 CMIP6 simulations, MPI-ESM1.2-HR) to or from NCEP SSTs. The pre-industrial simulations apply emissions of 1890 and the factual storylines the GHGs concentrations of RCP4.5 corresponding to their warming level. These boundary conditions can be specified with high confidence because both SSTs and GHG concentrations are strongly linked to anthropogenic forcing and are well understood in terms of their large-scale response characteristics. Each storyline consists of five ensemble members, and their spin-up simulations start on consecutive weeks to represent model and initial condition uncertainty.

#### Data ownership:
The simulations are created by the Institute of Coastal Systems, Helmholtz-Zentrum Hereon, Geesthacht, Germany. Contact with the working group is mandatory before usage of the data. The contact person is [Frauke Feser](mailto:Frauke.Feser@hereon.de).

#### Key literature:
* [van Garderen et al. (2021)](https://doi.org/10.5194/nhess-21-171-2021)
* [Feser et al. (2024)](https://doi.org/10.1175/BAMS-D-24-0017.1)

#### Available simulations:
| Simulation | Appreviation | Description | Covered timeperiod | Ensemble members |
| ------------- |-------------|-------------|-------------|-------------|
| Historical | Hist | 1950 boundary conditions | 2017‑2024 | 1 |
| Pre-industrial | Cont | recorded boundary conditions | 2017‑2024 | 1 |
|  | Tp2K | boundary conditions from a 2K warmer world | 2017‑2024 | 1 |

#### Overview of the available variables:
A variety of different atmospheric and ocean related variabels are saved at hourly and daily time scales. A full overview is provided at ??.

#### Access the data:
A DKRZ account is mandatory to access the data. A detailed description of how to download the data is provided in the Jupyter Notebook: [XX](XX).

