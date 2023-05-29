# WildFires_capstone

![WildFire Image](https://github.com/KeananG/WildFires_capstone/blob/main/mike-newbry-_AwSiaesk40-unsplash.jpg)
---

## Project Overview
The goal of this project is to develop a classification model that can predict the fire management complexity level of a wildfire. Fire management complexity represents the highest management level utilized to manage a wildland fire. This target provides valuable insights into the resources needed and the potential scale, size and impact of a fire.

The classification model analyzes various features associated with the a wildfire incident, including meteorological data, bureaucratic data, and locational data.

The developed classification model will enable fire management agencies to anticipate the resources required should a wildfire were to occur based on the location and current meteorological data. This model doesn't replace the realtime complex decision of determining fire management complexity level (like evaluating the risk to the firefighters). 

---

## Business Understanding

---

## Data Understanding
### Target: FireMgmtComplexity (Defined below under [Final Features](#final-features))
##### Factors contributing to the fire management complexity level:
  - Area involved
  - Threat to life and property
  - Political sensitivity
  - Organizational complexity
  - Jurisdictional boundaries
  - Values at risk
  - Fire behavior
  - Strategy and tactics
  - Agency policy
Source: https://gacc.nifc.gov/swcc/management_admin/Agency_Administrator/AA_Guidelines/pdf_files/ch5.pdf
##### FireMgmtComplexity classes:
The levels of wildfire fire incidents range from Type 5 to Type 1. Each level represents a specific level of complexity, with Type 5 being the lowest (local resources, 2-6 firefighters, quickly contained or low impact risk) and Type 1 being the most complex (500+ firefighters, aircraft and number other resources used, large scale). 

Fire management complexity can be used to further evaluate if a location is at risk of being resource intensive or potentially large threat to life and property should a wildfire occur.

### Data Sets

- Wildfire Occurrences
  - https://data-nifc.opendata.arcgis.com/datasets/nifc::wildland-fire-incident-locations/about
  - This dataset gets updated daily and contains data going back to roughly 2014
- Live RAWS Data
- Historical RAWS Data

### Final Features
  - FireMgmtComplexity: The highest management level utilized to manage a wildland fire
  -


---

## Data Preprocessing

<!--
Notes:
- Data Storage
- Preprocessing Steps 
-->

### EDA - Historical RAWS Data


### EDA - Fire Occurrences Data


### EDA - Final Dataset


---

## Modeling


---

## Performance


---

## Feature Importance


---

## Conclusion


---

## Next Steps


---

## Contact Information


---

## Repo Structure

