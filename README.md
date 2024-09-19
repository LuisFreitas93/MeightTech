# MeightTech


Meight Road Freight Price Analytics System

Scenario:

Meight tracks market prices for road freight services such as full-truck-load, less-than-truck-load, refrigerated services, and flatbeds across various European regions. The aim is to develop a system that computes analytics based on historical data to offer insights into road freight pricing.

Objective:

The project involves designing and building a data pipeline that processes and transforms historical road freight market prices. The system should enable analytics output filtered by pickup_region, delivery_region, trailer_type, and service_type, providing insights based on a substantial volume of records.

Challenge Steps:

	1.	Data Pipeline Scheduling and Automation:
		Objective: ETL pipeline to extract data from a mock API, clen the data and load it to a database. Automate the ETL pipeline using tools like Apache Airflow to ensure data is processed and updated on a regular schedule.
  
	2.	Analytics Integration:
		Objective: Generate analytics that return the 25th percentile, 75th percentile, and average of the user-selected input data.
  
	3.	Data Visualization and Reporting (in Progress):
		Objective: Provide visualizations for historical price trends by region and service type. Include forecasted prices and their comparison with actual prices, moving averages, price fluctuations, and market trends.

Setup and Installation

    For the ETL pipeline
	•	Clone the repository: git clone https://github.com/LuisFreitas93/MeightTech.git
	•	Install dependencies: pip install -r requirements.txt
	•	Run the ETL pipeline 

    For Analytics
    •	Go to Snowflake https://app.snowflake.com/tykejnb/aa50676/w5OXb6P3KEeB#query with credentials:
        user='LFREITASTRIAL',
        password='MeightTest1',
    •	Go to page and run the function with arguments
            road_freight_analytics_v1(service_type, trailer_type, pickup_coordinate, delivery_coordinate);


    For Scheduling (in progress)

    For Reporting (in progress)
