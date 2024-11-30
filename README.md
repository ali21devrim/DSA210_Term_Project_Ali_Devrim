# **Analysis of Physical Activity, Weather and Social Media Usage**
## **Project Description**
This project aims to examine the relationship between physical activity (number of steps), weather and social media use. The project aims to analyse how these three factors influence each other. In particular, it aims to analyse how weather conditions affect physical activity and how physical activity and social media use affect each other. As a result, it tries to understand whether there is an indirect relationship between weather and social media use.

## **Motivation**
My motivation for working on this project was to investigate the conditions under which I do physical activities such as walking and running, which I have recently added to my life, more often and whether these activities are beneficial in terms of productivity.

## **Datasets**
This project will utilise three main datasets:

### 1. Step Count Data:
* Data Source: Apple Health API
* Description: Daily step count data will be collected using the Apple Health API. Since the data is not shared on a daily basis but scattered, it will be organised by converting it to the total number of steps per day.
  
### 2. Weather Data:
* Data Source: Weatherstack API.
* Description: Daily weather data (temperature, wind speed, humidity, etc.) will be received from Weatherstach API. Since historical weather APIs are not accessible, historical data will be obtained manually from https://www.havaturkiye.com/.
  
### 3. Social Media Usage Data:
* Data Source: IPhone screen time reports.
* Description: Social media usage times will be recorded manually. This data will include time spent on platforms such as Instagram, TicToc and Twitter.
  
## **Project Plan**
### 1. Data Collection:
* Step Count Data: This will be fetched using an API daily.
* Weather Information: This will be filled in manually every day.
* Social Media Usage Information: The time spent using social media will be noted down daily manually.
  
### 2. Data Cleaning:
* The data will be checked until it is accurate and complete. Any incorrect, redundant or missing information will be deleted. Since this project does not investigate the dates before Novermber, 2024, datas which are belong pre November will be excluded.
  
### 3. Data Analysis:
* Collected data is subjected to two correlation study:
  * Physical activity and its association with weather conditions.
  *  Effects of physical acitivty upon social media usage.
* These hypotheses will be tested using statistical tests such as person correlation or t-test.
  
### 4. Visualisation of Results:
*  Visualizations like line graphs and scatter plots will be used to display the analysis results.
*  The graphs will graphically depict how the weather affects physical activity and social media useage consequently.
  
### 5. Conclusion and Comments:
*  When the project is completed, the findings will be evaluated and conclusions will be drawn based on the analyses.




