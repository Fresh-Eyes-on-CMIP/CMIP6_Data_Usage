# CMIP6_Data_Usage
Repo for the Fresh Eyes on CMIP project "CMIP6 Data Usage Report"


## Data
CVs data is a copy from https://github.com/PCMDI/cmip6-cmor-tables/tree/main/Tables and https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_table_id.json.
ESGF data was downloaded from https://esgf-ui.cmcc.it/esgf-dashboard-ui/cmip6.html 
C3S data was provided by Chris Goddard.
Initial CMIP6_Data_References.csv comes from https://www.wdc-climate.de/ords/f?p=127:2. It was then modified to include the number of citation found through DataCite.
country level population data is from the World Bank - https://data.worldbank.org/indicator/SP.POP.TOTL

## Instructions

1. Read the report (URL) and be so impressed that you want to reproduce the analysis.

2. Create a virtual environment.

```
    conda env create -f environment.yml
```

3. Run report-figures.ipynb


TODO: archive old scripts and maybe the figures.