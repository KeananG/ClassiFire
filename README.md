<!--# Wildfires Management Complexity Project-->
<h1 align="center">Wildfires Management Complexity Project</h1>


![WildFire Image](https://github.com/KeananG/WildFires_capstone/blob/main/mike-newbry-_AwSiaesk40-unsplash.jpg)
---

## Project Overview
  The goal of this project is to develop a classification model that can predict the fire management complexity level of a wildfire. Fire management complexity represents the highest management level utilized to manage a wildland fire. This target provides valuable insights into the resources needed and the potential scale, size and impact of a fire.

  This classification model analyzes various features associated with the a wildfire incident, including meteorological data, bureaucratic data, and locational data. The developed classification model will enable fire management agencies to anticipate the resources required should a wildfire occur based on the location and current meteorological data. This model doesn't replace the realtime complex decision of determining fire management complexity level (like evaluating the risk to the firefighters). However this model can aid in helping predict if a new wildfire incident will be a large scale/impacting event based on the predicted fire management complexity.

---

## Business Understanding

<!--In this section, explore the business understanding of the project, focusing on the value it provides and the real-world problem it addresses. The business understanding assesses how well the project explains the significance of the problem and its stakeholders.-->

Wildfires pose a significant risks to life, property, and the environment. Effective fire management is crucial for mitigating these risks and minimizing the impact of wildfires. Predicted fire management complexity level evaluates if a location is at risk of being resource intensive or potentially large threat to life and property should a wildfire occur. This can help identify regions that need to be on high alert and preparedness to minimize the impact of a wildfire.

The fire agencies administrator is responsible for setting the fire managment complexity level. Their decision follows a set of standarized and subjective guidelines. Some of these guidelines are utilized as features in this project. 

Fire management agencies, administrators, and other personnel responsible for allocating resources and planning fire response strategies would benefit from being able to accurately and efficiently predict the fire management complexity level of wildland fire incidents. This allows for them to anticipate the required resources, as well as assess the potential scale and impact of a fire. This information is crucial for fire management agencies to make informed decisions and ensured preparedness for faster fire response times.

<!-- It is important to note that the assessment of the business understanding focuses on how well the project explains its value and addresses a real-world problem, rather than evaluating the intrinsic value itself. By effectively conveying the significance of the problem and its stakeholders, the project demonstrates its relevance and practicality -->


---

## Data Understanding
Data is stored in several formats, uploaded
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
##### FireMgmtComplexity Classes:
The levels of wildfire fire incidents range from Type 5 to Type 1. Each level represents a specific level of complexity, with Type 5 being the lowest (local resources, 2-6 firefighters, quickly contained or low impact risk) and Type 1 being the most complex (500+ firefighters, aircraft and number other resources used, large scale). 

### Data Sets
The data used in this project comes from the following sources below:
- Wildfire Occurrences
  - https://data-nifc.opendata.arcgis.com/datasets/nifc::wildland-fire-incident-locations/about
  - This dataset gets updated daily and contains data going back to roughly 2014
- Live RAWS Data
  - https://data-nifc.opendata.arcgis.com/datasets/nifc::public-view-interagency-remote-automatic-weather-stations-raws/about
  - Dataset of live RAWS data
- Historical RAWS Data
  - https://raws.dri.edu/
  - Contains historical data for around 3k RAWS 
- Elevation data:
  - open elevation api 
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
```
├── Images (for readme, presentation)
├── Final Presentation (pdf Presentation)
├── web_scraper.ipynb
├── post_request.ipynb
├── EDA1.ipynb
├── Modeling_Notebook.ipynb
├── Dataset Folder (dataset)
└── README.md
```
