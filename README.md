<!--#Wildfires Management Complexity Project-->
<h1 align="center">ClassiFire</h1>
<h2 align="center">Wildfires Management Complexity Project</h2>

![WildFire Image](images/mike-newbry-_AwSiaesk40-unsplash.jpg)
 _Image source: https://unsplash.com/@mikenewbry_
 
---
# Project Overview
  The goal of this project is to develop a classification model that can predict the fire management complexity level of a wildfire. Fire management complexity represents the highest management level utilized to manage a wildland fire. This target provides valuable insights into the resources needed and the potential scale, size, and impact of a fire.

  This classification model analyzes various features associated with a wildfire incident, including meteorological data, bureaucratic data, and locational data. The developed classification model will enable fire management agencies to anticipate the resources required should a wildfire occur based on the location and current meteorological data. This model doesn't replace the realtime complex decision of determining fire management complexity level (like evaluating the risk to the firefighters). However this model can aid in helping predict if a new wildfire incident will be a large scale/impacting event based on the predicted fire management complexity.

---
# Business Understanding

<!--In this section, explore the business understanding of the project, focusing on the value it provides and the real-world problem it addresses. The business understanding assesses how well the project explains the significance of the problem and its stakeholders.-->

Wildfires pose significant risks to life, property, and the environment. Effective fire management is crucial for mitigating these risks and minimizing the impact of wildfires. Predicted fire management complexity level evaluates if a location is at risk of being resource intensive or potentially large threat to life and property should a wildfire occur. This can help identify regions that need to be on high alert and preparedness to minimize the impact of a wildfire.

The fire agencies administrator is responsible for setting the fire managment complexity level. Their decision follows a set of standarized and subjective guidelines. Some of these guidelines are utilized as features in this project. 

Fire management agencies, administrators, and other personnel responsible for allocating resources and planning fire response strategies would benefit from being able to accurately and efficiently predict the fire management complexity level of wildland fire incidents. This allows for them to anticipate the required resources, as well as assess the potential scale and impact of a fire. This information is crucial for fire management agencies to make informed decisions and ensured preparedness for faster fire response times.

<!-- It is important to note that the assessment of the business understanding focuses on how well the project explains its value and addresses a real-world problem, rather than evaluating the intrinsic value itself. By effectively conveying the significance of the problem and its stakeholders, the project demonstrates its relevance and practicality -->
---
# Data Understanding
  - [Target](#Target)
  - [Data Sources](#data-sources)
  - [Data Directory](#data-directory)
  - [Key Features](#key-features)
## Target
  - FireMgmtComplexity ([Definition](#key-features))
#### Factors contributing to the fire management complexity level:
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
#### FireMgmtComplexity Classes:
The levels of wildfire fire incidents range from Type 5 to Type 1. Each level represents a specific level of complexity. 
Roughly 91% of fires are incident types 5 or type 4.
- Type 5:
  - lowest class
  - local resources 
  - 2-6 firefighters
  - quickly contained
  - low impact risk
- Type 4
  - Local resources
  - low impact risk
  - slight increase in scale compared to Type 5
- Type 3
  - Mix of local and regional resources used
  - increased scale and risk
  - action plan created
- Type 2
  - large scale 200+ firefighters
  - Many units required
  - regular planning and briefing
- Type 1 
  - highest class
  - Same characteristics of type 2 incident
  - 500+ firefighters
  - aircraft and aviation is used
  - Greater access to resources
  - larger scale and impact 
## Data Sources
The data used in this project comes from the following sources below:
- Wildfire Occurrences
  - https://data-nifc.opendata.arcgis.com/datasets/nifc::wildland-fire-incident-locations/about
  - This dataset gets updated daily and contains data going back to roughly 2014
- Live RAWS Data (Remote Access Weather Stations)
  - https://data-nifc.opendata.arcgis.com/datasets/nifc::public-view-interagency-remote-automatic-weather-stations-raws/about
  - Dataset of live RAWS data
- Historical RAWS Data
  - https://raws.dri.edu/
  - Contains historical data for around 3k RAWS 
- Elevation data:
  - open elevation api 
## Data Directory 
<!--| Data | Curation | Utilization | Additional Info |
|----------|----------|----------|----------------|
| station_list.csv    | web_scraper.ipynb    | post_request.ipynb    | RAWS 4-digit code |
| threshold_year.pickle    | web_scraper.ipynb   | EDA1.ipynb    | RAWS code and final year station collected data|
| nessid.csv    | web_scraper.ipynb    | EDA1.ipynb    | NESSID and RAWS code|
| RAWS_Historical_Full    | post_request.ipynb   | EDA1.ipynb    |Json files split into 4 files|
| RAWS.csv    | Live RAWS download    | ClassiFire.ipynb    ||
| stations_dates.csv.zip    | EDA1.ipynb    | ClassiFire.ipynb    | Row corresponds to a day, column represents a RAWS. Missing data for a RAWS on a specific day is denoted as null.|
| RAWS_stations.csv.zip    | EDA1.ipynb    | ClassiFire.ipynb    |This is split up into 1,2 and 3, Use pd.concat([1,2,3], axis=1) in notebook|
| Wildland_Fire_Incident_Locations.csv.zip    | Wildfire Occurrences download    | ClassiFire.ipynb   ||
| clean_fire_data.csv.zip  | ClassiFire.ipynb   | ClassiFire.ipynb   ||
| fire_elevation.csv  | ClassiFire.ipynb   | ClassiFire.ipynb   |Elevation of each fire incident|
| fire_model_data.csv  | ClassiFire.ipynb   | ClassiFire.ipynb   |Final dataset used to Model, drop unwanted columns before modeling|-->
   <table>
    <tr>
      <th>Data</th>
      <th>Curation</th>
      <th>Utilization</th>
      <th>Additional Info</th>
    </tr>
    <tr>
      <td>station_list.csv</td>
      <td>web_scraper.ipynb</td>
      <td>post_request.ipynb</td>
      <td>RAWS 4-digit code</td>
    </tr>
    <tr>
      <td>threshold_year.pickle</td>
      <td>web_scraper.ipynb</td>
      <td>EDA1.ipynb</td>
      <td>RAWS code and final year station collected data</td>
    </tr>
    <tr>
      <td>nessid.csv</td>
      <td>web_scraper.ipynb</td>
      <td>EDA1.ipynb</td>
      <td>NESSID and RAWS code</td>
    </tr>
    <tr>
      <td>RAWS_Historical_Full</td>
      <td>post_request.ipynb</td>
      <td>EDA1.ipynb</td>
      <td>Json files split into 4 files</td>
    </tr>
    <tr>
      <td>RAWS.csv</td>
      <td>Live RAWS download</td>
      <td>Modeling.ipynb</td>
      <td></td>
    </tr>
    <tr>
      <td>stations_dates.csv.zip</td>
      <td>EDA1.ipynb</td>
      <td>Modeling.ipynb</td>
      <td>Row corresponds to a day, column represents a RAWS. Missing data for a RAWS on a specific day is denoted as null.</td>
    </tr>
    <tr>
      <td>RAWS_stations.csv.zip</td>
      <td>EDA1.ipynb</td>
      <td>Modeling.ipynb</td>
      <td>This is split up into 1, 2, and 3. Use pd.concat([1, 2, 3], axis=1) in the notebook.</td>
    </tr>
    <tr>
      <td>Wildland_Fire_Incident_Locations.csv.zip</td>
      <td>Wildfire Occurrences download</td>
      <td>Modeling.ipynb</td>
      <td></td>
    </tr>
    <tr>
      <td>clean_fire_data.csv.zip</td>
      <td>Modeling.ipynb</td>
      <td>Modeling.ipynb</td>
      <td></td>
    </tr>
    <tr>
      <td>fire_elevation.csv</td>
      <td>Modeling.ipynb</td>
      <td>Modeling.ipynb</td>
      <td>Elevation of each fire incident</td>
    </tr>
    <tr>
      <td>fire_model_data.csv</td>
      <td>Modeling.ipynb</td>
      <td>Modeling.ipynb</td>
      <td>Final dataset used to Model, drop unwanted columns before modeling</td>
    </tr>
  </table>
  
## Key Features
Below are the key features used in this project. Several features in the dataset have corresponding features that contained the same or similar data. These features were utilized to fill in missing values whenever possible. There are many more features then what is listed here, refer to source websites for an indepth overview.
### Fire Incidents:
Definitions provided by source
- **FireMgmtComplexity:** The highest management level utilized to manage a wildland fire

- **FinalAcres:** Final burn acres, nulls filled in with IncidentSize
- **site:** Created in ClassiFire.ipynb, closest RAWS that has at least 50% data coverage over the duration of a fire incident. 
  -  It is used as a reference point for analyzing weather conditions during the fire event.
-  **DispatchCenterID:** A unique identifier for a dispatch center responsible for supporting the incident. Nulls filled in with POODispatchCenterID
-  **POODispatchCenterID:** A unique identifier for the dispatch center that intersects with the incident point of origin (point where fire incident occured)
- **POOJurisdictionalAgency:** The agency having land and resource management responsibility for a fire incident as provided by federal, state or local law
- **POOFips:** Code identifies counties and county equivalents. The first two digits are the FIPS State code and the last three are the county code within the state.
- **FireDiscoveryDateTime:** The date and time a fire was reported as discovered or confirmed to exist
- **FireOutDateTime:** The date and time when a fire is declared out
- **OBJECTID:** Incident ID for dataset
- **EstimatedFinalCost:** Nulls filled in with EstimatedCostTodate
- **elevation:** Elevation of fire incident (meters) 
### RAWS data:
For each fire incident, all meteorological metrics were computed as averages of the fire duration.
  - **NESSID:**  NESS ID for identifying RAWS
  
  - **X:** Longitude
  - **Y:** Latitude
  - **date:** date when data was collected, if null then no data collected on that day
  - **total_solar_radiation_ly:** Solar radiation
  - **ave_mean_wind_speed_mph:** Average wind speed (mph)
  - **ave_mean_wind_direction_deg:** Average wind direction (degree)
  - **max_maximum_wind_gust_mph:** Maximum wind gust (mph)
  - **ave_average_air_temperature_deg_f:** Average air temperature (ºF)
  - **ave_average_relative_humidity:** Average relative humidity
  - **total_precipitation_in:** Total precipitation (inches)
  
  Data Set length: over 250K and the final model dataset has a length of 7731
  RAWS: There are roughly 2252 RAWS sites with usable data, aaround 3k in total
  
---
# Project Rundown
- All needed data is saved under data folder refer to each notebook to import those datasets
- refer to [Data Directory](#data-directory) for dataset source/curation and where its used.
 1. Run model [ClassiFire notebook](ClassiFire.ipynb) up until Thiessen Polygon, this provides a general overview of the fire incident occurences and features
 2. Webscrape urls, nessids, RAWS code, and more 
 [web scraping  notebook](web_scraper.ipynb)
 3. Mimics post request to pull RAWS historial data from 2014-2023 
 [post request notebook](post_request.ipynb)
 4. Load in RAWS json files, creates 2 dataframes for further EDA and cleaning, a simple data cleaning is performed to reduce datasize 
[EDA1 notebook](EDA1.ipynb) I
 5. Continue with [ClassiFire notebook](ClassiFire.ipynb) Further EDA, generates meteorological attributes for each fire, modeling, and evalutaion, This is the main notebook 

--- 
# Data Preprocessing
- Rough synopsis of the data preprocessing invloved for each data set
<!--
Notes:
- Data Storage
- Preprocessing Steps 
-->
## Historical RAWS Data
- Changed -9999 values to nulls
- Dropped rows that are beyond each stations data collecting time period
- Created dataframes where each column is a RAWS and row inputs are days, if data doesn't exist for that date then a null is placed, 
- Changed the 4 digit code used generating the post request to the stations NESS ID 
- fixed datetimes columns
- Removed RAWS that contained no data from 2014 to 2023
## Fire Occurrences Data
- Dropping duplicates
- Dropped fires where end date was before the start date and other irregularities 
- Only used fires that occured within the contiguous USA
- fixed datetimes columns
- Filled in nulls with values from corresponding features when possible 
## Final Dataset
- Calculated the mean meteorological metrics for each fire
- Dropped nulls
- fixed datetimes columns
- Created dataseet with only the key features

![Fire Site Map](images/fire_site_map.png)
The map illustrates the spatial relationship between the fire incidents utilized in ClassiFire and the corresponding remote access weather station (RAWS) from which meteorological attributes are obtained. The red lines on the map depict the fires that are among the top 1% farthest from the RAWS sites. The red shading serves to highlight their significant distance from the respective RAWS.

---

# Modeling
A Random forest classifier, decision tree and dummy model were used
![scores](images/white/scores.png)

---

# Performance
![Incident Scores](images/white/Incident_scores.png)

![Red Confusion Matrix](images/white/matrix_red_w.png)

---

# Feature Importance
![Feature Importance](images/white/feature_importance.png)


---

# Conclusion

### The final model scores: 
<!--|Complexity level  | precision | recall | f1-score | support |
|----------------|-----------|--------|----------|---------|
| Type 1 Incident |   0.75    |  0.60  |   0.67   |    10   |
| Type 2 Incident |   0.11    |  0.08  |   0.10   |    12   |
| Type 3 Incident |   0.39    |  0.25  |   0.30   |   124   |
| Type 4 Incident |   0.65    |  0.81  |   0.72   |   467   |
| Type 5 Incident |   0.96    |  0.91  |   0.94   |   1320  |
| accuracy       |           |        |   0.84   |   1933  |
| macro avg      |   0.57    |  0.53  |   0.54   |   1933  |
| weighted avg   |   0.84    |  0.84  |   0.84   |   1933  |-->
<table>
  <tr>
    <th>Complexity level</th>
    <th>precision</th>
    <th>recall</th>
    <th>f1-score</th>
    <th>support</th>
  </tr>
  <tr>
    <td>Type 1 Incident</td>
    <td>0.75</td>
    <td>0.60</td>
    <td>0.67</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Type 2 Incident</td>
    <td>0.11</td>
    <td>0.08</td>
    <td>0.10</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Type 3 Incident</td>
    <td>0.39</td>
    <td>0.25</td>
    <td>0.30</td>
    <td>124</td>
  </tr>
  <tr>
    <td>Type 4 Incident</td>
    <td>0.65</td>
    <td>0.81</td>
    <td>0.72</td>
    <td>467</td>
  </tr>
  <tr>
    <td>Type 5 Incident</td>
    <td>0.96</td>
    <td>0.91</td>
    <td>0.94</td>
    <td>1320</td>
  </tr>
  <tr>
    <td>accuracy</td>
    <td></td>
    <td></td>
    <td>0.84</td>
    <td>1933</td>
  </tr>
  <tr>
    <td>macro avg</td>
    <td>0.57</td>
    <td>0.53</td>
    <td>0.54</td>
    <td>1933</td>
  </tr>
  <tr>
    <td>weighted avg</td>
    <td>0.84</td>
    <td>0.84</td>
    <td>0.84</td>
    <td>1933</td>
  </tr>
</table>


The final model performs best at predicting type 5 incidents, even though I used smote, the majority of wildfires occur at the type 5 incident. This means that most fires are put out within a few days and or only require a few firefighters.
Type 4 incident is one level up and type 1 incidents have the next best performance. With type 2 and 3 performing poorly. Looking at the usability of this model it is more significant to be able to predict both extremes well. 
If a fire incident is 1 day old it is likely still at type 5, this model will be able to use current and forecasted meteorological data, and bureaucratic features such as agency and dispatch center to predict the fire incidents fire complexity level. Further evaluation shows that the highest mean acres burned and economic cost correlate with type 1 incidents, This for one confirms that fire complexity levels do correlate with fire scale and impact. However, this is not absolute, when evaluating the max acres burned for each level types 1, 3, and 5 all share close max acres burned. This could be an error in the data or Possibly more underlying factors influencing the fire complexity level. One speculation is that large fires occurring in heavily remote regions are less of a risk to people and communities. Further analysis also shows that type 4 incidents have the largest cumulative acres burned and economic costs. This is likely due to just the class imbalance as the mean shows that type 1 incidents are significantly higher in both features.

![Target Acres Max](images/white/Target_Acres_max.png)
![Target Elevation Mean](images/white/Target_Elevation_mean.png)
![Target Acres Mean](images/white/Target_acres_mean.png)
![Target Acres Sum](images/white/Target_acres_sum.png)
![Target Cost Mean](images/white/Target_cost_mean.png)
![Target Cost Sum](images/white/Target_cost_sum.png)


# Heat Map Over Time 

18,000 of 250,000 fires occuring between 2014 - 2023 in the contiguous USA

[Wildfire occurrences Heat Map](https://keanang.github.io/ClassiFire/images/Heat_map.html)

---

# Next Steps

Looking at the next steps, I am looking to further improve model performance by adding additional features such as calculating drought data, remoteness index, and improving RAWS site selection. After this, I am looking to build a streamlit deployment of the model. This will involve setting up APIs and pulling current RAWS data, and potentially forecasted Meteorological data.

---

# Contact Information

## Email:  
ginell_k1@denison.edu

## Github: 
[github.com/KeananG](https://github.com/KeananG/)

## Linkedin: 
[linkedin.com/in/keanan-ginell](https://www.linkedin.com/in/keanan-ginell)


---

# Repo Structure
```
├── .gitignore
├── ClassiFire.ipynb
├── ClassiFire_presentation.pdf
├── Data
│   ├── RAWS.csv
│   ├── RAWS_Historical_Full
│   │   ├── set1.zip
│   │   ├── set2.zip
│   │   ├── set3.zip
│   │   ├── set4.zip
│   ├── RAWS_stations1.csv.zip
│   ├── RAWS_stations2.csv.zip
│   ├── RAWS_stations3.csv.zip
│   ├── Wildland_Fire_Incident_Locations.csv.zip
│   ├── clean_fire_data.csv.zip
│   ├── fire_elevation.csv
│   ├── fire_model_data.csv
│   ├── nessid.csv
│   ├── station_list.csv
│   ├── stations_dates.csv.zip
│   ├── threshold_year.pickle
├── EDA1.ipynb
├── LICENSE
├── README.md
├── environment.yml
├── heatmap.ipynb
├── images
│   ├── Heat_map.html
│   ├── Incident_scores.png
│   ├── Target_Acres_max.png
│   ├── Target_Elevation_mean.png
│   ├── Target_acres_mean.png
│   ├── Target_acres_sum.png
│   ├── Target_cost_mean.png
│   ├── Target_cost_sum.png
│   ├── feature_importance.png
│   ├── fire_site_map.png
│   ├── matrix.png
│   ├── matrix_red.png
│   ├── mike-newbry-_AwSiaesk40-unsplash.jpg
│   ├── scores.png
│   ├── white
│       ├── Incident_scores.png
│       ├── Target_Acres_max.png
│       ├── Target_Elevation_mean.png
│       ├── Target_acres_mean.png
│       ├── Target_acres_sum.png
│       ├── Target_cost_mean.png
│       ├── Target_cost_sum.png
│       ├── feature_importance.png
│       ├── matrix_red_w.png
│       ├── scores.png
├── index.md
├── notebook.pdf
├── post_request.ipynb
├── update_readme.py
├── web_scraper.ipynb
```
