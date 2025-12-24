US Real Estate Insights Dashboard



Overview

--------

This project presents a data-driven analytics dashboard for exploring housing affordability and pricing trends across United States cities and states.



It integrates public demographic data with housing market data to enable structured comparison of cities by population size, median home value, and relative affordability. The project demonstrates an end-to-end analytics workflow, from data ingestion and processing to exploratory analysis and interactive visualisation.



Objectives

----------

• Compare median home values across U.S. cities and states  

• Identify relatively affordable and expensive housing markets  

• Examine the relationship between city population size and housing prices  

• Provide an interactive interface for exploring real estate trends  



Target Users

------------

• U.S. home buyers seeking market comparisons  

• Real estate professionals requiring contextual pricing insights  

• Property investors evaluating location-based opportunities  



Business Context

----------------

U.S. Residential Real Estate



Housing prices in the United States vary significantly by geography, population size, and market dynamics. Buyers and professionals often rely on fragmented sources, making consistent comparison difficult.



Value Delivered

---------------

• Faster market comparison across cities and states  

• Data-backed context for pricing discussions  

• Improved identification of affordable or high-growth locations  



Data Sources

------------

City Population Data

Source: Wikipedia – List of United States cities by population  

Reference Year: 2024 (latest fully validated estimates)



Population data for 2025 is still provisional across many sources. Using 2024 ensures consistency, reliability, and comparability across all cities.



Housing Price Data

Source: Zillow Research – Zillow Home Value Index (ZHVI)  

Metric: Median (typical) home value by city  

Latest Period Used: November 2025  



Project Structure

-----------------

us-real-estate-dashboard

│

├── app.py                     Streamlit application

├── src                         Data processing scripts

│   ├── scrape\_us\_cities.py

│   ├── clean\_us\_cities.py

│   ├── build\_affordability\_metrics.py

│

├── data

│   ├── raw                     Raw input data

│   ├── processed               Cleaned and enriched datasets

│   └── external                Zillow ZHVI data

│

├── outputs

│   └── figures                 Generated charts and plots

│

├── notebooks                   Exploratory analysis

├── requirements.txt

├── README.md

└── .gitignore



Data Pipeline

-------------

1\. Data Collection  

&nbsp;  • Extracted U.S. city population tables from Wikipedia  

&nbsp;  • Ingested Zillow ZHVI city-level home value data  



2\. Data Cleaning and Standardisation  

&nbsp;  • Normalised city and state identifiers  

&nbsp;  • Selected consistent population metrics  

&nbsp;  • Removed incomplete or irrelevant records  

&nbsp;  • Added metadata for transparency:

&nbsp;    - population\_year

&nbsp;    - scraped\_date

&nbsp;    - data\_source  



3\. Feature Engineering  

&nbsp;  • Categorised cities by population size (Small to Mega)  

&nbsp;  • Computed affordability rankings within each category  

&nbsp;  • Flagged cities as relatively affordable or expensive within peer groups  



4\. Exploratory Analysis  

&nbsp;  • Distribution of city populations  

&nbsp;  • Distribution of median home values  

&nbsp;  • Population versus price relationship  

&nbsp;  • City-size-based affordability comparisons  



5\. Interactive Dashboard  

&nbsp;  • Built using Streamlit  

&nbsp;  • State- and city-level filtering  

&nbsp;  • Dynamic metrics and visualisations  

&nbsp;  • Reactive updates without page reload  



Key Visualisations

------------------

• Population distribution across U.S. cities  

• Median home value distribution  

• Population versus housing price comparison  

• Affordability rankings by city size  

• City count and median prices by state  



All figures are stored under outputs/figures for reproducibility.



Running the Dashboard Locally

-----------------------------

python -m venv .venv  

.\\.venv\\Scripts\\Activate.ps1  

pip install -r requirements.txt  

streamlit run app.py  



The application launches at http://localhost:8501



Assumptions and Limitations

---------------------------

• Population figures reflect 2024 estimates, not real-time counts  

• Zillow ZHVI represents typical home values, not individual listings  

• The project focuses on exploratory analysis and decision support  

• No predictive modeling or forecasting is performed  



Technical Skills Demonstrated

-----------------------------

• Python (pandas, numpy, matplotlib)  

• Web data extraction and ingestion  

• Data cleaning and validation  

• Exploratory Data Analysis  

• Statistical interpretation  

• Data visualisation  

• Streamlit dashboard development  

• Reproducible project structuring  

• Git and GitHub version control  



Scope Statement

---------------

This project supports comparative analysis of U.S. city-level housing affordability using public datasets. The emphasis is on data quality, interpretability, and interactive exploration rather than predictive modeling or production deployment.



Potential Extensions

--------------------

• Incorporate rental price data  

• Integrate income or wage statistics  

• Add geographic map-based visualisations  

• Deploy the dashboard via Streamlit Cloud  



Author

------

Sri Harsha Gorantla

US Real Estate Insights Dashboard



Overview

--------

This project presents a data-driven analytics dashboard for exploring housing affordability and pricing trends across United States cities and states.



It integrates public demographic data with housing market data to enable structured comparison of cities by population size, median home value, and relative affordability. The project demonstrates an end-to-end analytics workflow, from data ingestion and processing to exploratory analysis and interactive visualisation.



Objectives

----------

• Compare median home values across U.S. cities and states  

• Identify relatively affordable and expensive housing markets  

• Examine the relationship between city population size and housing prices  

• Provide an interactive interface for exploring real estate trends  



Target Users

------------

• U.S. home buyers seeking market comparisons  

• Real estate professionals requiring contextual pricing insights  

• Property investors evaluating location-based opportunities  



Business Context

----------------

U.S. Residential Real Estate



Housing prices in the United States vary significantly by geography, population size, and market dynamics. Buyers and professionals often rely on fragmented sources, making consistent comparison difficult.



Value Delivered

---------------

• Faster market comparison across cities and states  

• Data-backed context for pricing discussions  

• Improved identification of affordable or high-growth locations  



Data Sources

------------

City Population Data

Source: Wikipedia – List of United States cities by population  

Reference Year: 2024 (latest fully validated estimates)



Population data for 2025 is still provisional across many sources. Using 2024 ensures consistency, reliability, and comparability across all cities.



Housing Price Data

Source: Zillow Research – Zillow Home Value Index (ZHVI)  

Metric: Median (typical) home value by city  

Latest Period Used: November 2025  



Project Structure

-----------------

us-real-estate-dashboard

│

├── app.py                     Streamlit application

├── src                         Data processing scripts

│   ├── scrape\_us\_cities.py

│   ├── clean\_us\_cities.py

│   ├── build\_affordability\_metrics.py

│

├── data

│   ├── raw                     Raw input data

│   ├── processed               Cleaned and enriched datasets

│   └── external                Zillow ZHVI data

│

├── outputs

│   └── figures                 Generated charts and plots

│

├── notebooks                   Exploratory analysis

├── requirements.txt

├── README.md

└── .gitignore



Data Pipeline

-------------

1\. Data Collection  

&nbsp;  • Extracted U.S. city population tables from Wikipedia  

&nbsp;  • Ingested Zillow ZHVI city-level home value data  



2\. Data Cleaning and Standardisation  

&nbsp;  • Normalised city and state identifiers  

&nbsp;  • Selected consistent population metrics  

&nbsp;  • Removed incomplete or irrelevant records  

&nbsp;  • Added metadata for transparency:

&nbsp;    - population\_year

&nbsp;    - scraped\_date

&nbsp;    - data\_source  



3\. Feature Engineering  

&nbsp;  • Categorised cities by population size (Small to Mega)  

&nbsp;  • Computed affordability rankings within each category  

&nbsp;  • Flagged cities as relatively affordable or expensive within peer groups  



4\. Exploratory Analysis  

&nbsp;  • Distribution of city populations  

&nbsp;  • Distribution of median home values  

&nbsp;  • Population versus price relationship  

&nbsp;  • City-size-based affordability comparisons  



5\. Interactive Dashboard  

&nbsp;  • Built using Streamlit  

&nbsp;  • State- and city-level filtering  

&nbsp;  • Dynamic metrics and visualisations  

&nbsp;  • Reactive updates without page reload  



Key Visualisations

------------------

• Population distribution across U.S. cities  

• Median home value distribution  

• Population versus housing price comparison  

• Affordability rankings by city size  

• City count and median prices by state  



All figures are stored under outputs/figures for reproducibility.



Running the Dashboard Locally

-----------------------------

python -m venv .venv  

.\\.venv\\Scripts\\Activate.ps1  

pip install -r requirements.txt  

streamlit run app.py  



The application launches at http://localhost:8501



Assumptions and Limitations

---------------------------

• Population figures reflect 2024 estimates, not real-time counts  

• Zillow ZHVI represents typical home values, not individual listings  

• The project focuses on exploratory analysis and decision support  

• No predictive modeling or forecasting is performed  



Technical Skills Demonstrated

-----------------------------

• Python (pandas, numpy, matplotlib)  

• Web data extraction and ingestion  

• Data cleaning and validation  

• Exploratory Data Analysis  

• Statistical interpretation  

• Data visualisation  

• Streamlit dashboard development  

• Reproducible project structuring  

• Git and GitHub version control  



Scope Statement

---------------

This project supports comparative analysis of U.S. city-level housing affordability using public datasets. The emphasis is on data quality, interpretability, and interactive exploration rather than predictive modeling or production deployment.



Potential Extensions

--------------------

• Incorporate rental price data  

• Integrate income or wage statistics  

• Add geographic map-based visualisations  

• Deploy the dashboard via Streamlit Cloud  



Author

------

Vineela Bathula



