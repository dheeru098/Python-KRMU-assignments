echo # Weather Data Analysis – Summary Report

## 1. Introduction
In this project, I worked with a small weather dataset to understand basic patterns in temperature, humidity, and rainfall. After cleaning the data and converting the date column properly, I grouped the records by month so that I could compare how the weather changed between January and February.

## 2. Data Export
Once the cleaning and preprocessing steps were completed, I saved the final version of the dataset as:
cleaned_weather.csv

## 3. Monthly Grouping & Aggregation
To study monthly behavior, I created a new Month column from the Date and used Pandas groupby to calculate monthly totals and comparisons. This helped show how rainfall and temperature differed between January and February.

## 4. Saved Visualizations
The required plots were generated using Matplotlib and saved as PNG files:
- temp_trend.png
- monthly_rainfall.png
- humidity_vs_temp.png
- combined_plot.png

## 5. Insights and Interpretation
From the analysis:
- Temperatures increased slightly from January to February.
- February received more rainfall overall.
- Humidity was lower on warmer days.
These insights helped me understand simple weather patterns from the dataset.
