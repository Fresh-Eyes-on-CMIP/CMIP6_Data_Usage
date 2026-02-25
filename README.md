# CMIP6 Data Usage
Repo for the Fresh Eyes on CMIP project "CMIP6 Data Usage Report".

The report was submitted under the name "CMIP6 data usage: Lessons learned from more than 200 million downloads" to the GMD CMIP7 Special Issue.

DOI TO COME.


## Data
* CVs data is a copy from https://github.com/PCMDI/cmip6-cmor-tables/tree/main/Tables and https://github.com/WCRP-CMIP/CMIP6_CVs/blob/main/CMIP6_table_id.json.
* ESGF data was downloaded from https://esgf-ui.cmcc.it/esgf-dashboard-ui/cmip6.html 
* C3S data was provided by Chris Goddard.
* AWS data was provided by Aparna Radhakrishnan.
* Initial CMIP6_Data_References.csv comes from https://www.wdc-climate.de/ords/f?p=127:2. It was then modified to include the number of citation found through DataCite.
* Country level population data is from the World Bank - https://data.worldbank.org/indicator/SP.POP.TOTL

## Instructions

1. Read the report (URL) and be so impressed that you want to reproduce the analysis.

2. Create a virtual environment.

```
    conda env create -f environment.yml
```

3. Run report-figures.ipynb



## Acknowledgments

The authors would like to thank the team of the CMCC ESGF Data Statistics service, specifically Alessandra Nuzzo, Sandro Luigi Fiore, Fabrizio Antonio, and Paola Nassisi , who assisted us with our analysis and arising questions. Further, we thank Christopher Goddard, Aparna Radhakrishnan and Kristopher Rand, for provision of and information on data for C3S, Pangeo and AWS , as well as their insightful comments on a draft of the manuscript. We particularly want to thank Julius Busecke for numerous knowledgeable comments and suggestion on our manuscript. We would also like the thank the IPO, especially Beth Dingley, for their administrative help and the members of the Fresh Eyes steering group, such as Douglas Rao,  for their support and comments. Further, we acknowledge the previous members of the Infrastructure and Technical Fresh Eyes subgroup that participated in initial discussions and brainstorming on the project, particularly Rob Junod, ex-member of  the Infrastructure and Technical Fresh Eyes subgroup and CMIP6 usage report project, who did some initial analysis on model usage in ESGF. Finally, we would  like to thank the former and current co-leads of the WCRP ESMO Infrastructure Panel (WIP) Paul Durack and Matthew Mizielinski who suggested this project. 
