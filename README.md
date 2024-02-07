# Molecular Coal Structure Database for Monarch,Herrin,Springfield and Blue Gem

Coal molecular database contructed from molecularsolidbuilder with four coal samples

This repository contains the molecular structures generated from the MolecularSolidBuilder tool (https://github.com/MoleCraftHUB/MolecularSolidBuilder).

### Database repository structure

    .
    ├── Exp_data/
    │   ├── Coal_Element.csv              # csv file for experimental elemental composition data
    │   ├── Coal_Mass_Distribution.csv    # csv file for experimental mass distribution data
    │   └── Coal_NMR.csv                  # csv file for experimental 13C-NMR data
    ├── Monarch/                          
    │   ├── Condensed_Data/               # xyz files for gas and solid phase for the coal model
    │   ├── Model_Construction/           # jupyter notebook example for construction workflow using MolecularSolidBuilder tool
    │   └── Molecular_Data/               # xyz files for individual molecules in each range of molecular weight
    ├── Herrin/                    
    │   ├── Condensed_Data/               # xyz files for gas and solid phase for the coal model
    │   └── Molecular_Data/               # xyz files for individual molecules in each range of molecular weight
    ├── Springfield/                    
    │   ├── Condensed_Data/               # xyz files for gas and solid phase for the coal model
    │   └── Molecular_Data/               # xyz files for individual molecules in each range of molecular weight
    ├── Blue Gem/                    
    │   ├── Condensed_Data/               # xyz files for gas and solid phase for the coal model
    │   ├── Molecular_Data/               # xyz files for individual molecules in each range of molecular weight
    │   ├── ReaxFF_Mattsson/              # xyz files at t=0ns and t=1ns of 2073 K ReaxFF simulations using Mattsson parameter
    │   └── ReaxFF_Nielson/               # xyz files at t=0ns and t=1ns of 2073 K ReaxFF simulations using Nielson parameter
    └── images/

### Experimental data VS atomistic model data

<img src="./images/exp-VS-model_13cnmr.png" width="400">

<img src="./images/exp-VS-model_Elements.png" width="400">

<img src="./images/exp-VS-model_Mass-distribution.png" width="400">

<img src="./images/exp-VS-model_IRspectra.png" width="400">


