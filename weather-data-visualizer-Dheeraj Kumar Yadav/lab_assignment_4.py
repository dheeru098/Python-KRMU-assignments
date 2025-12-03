import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("python/weather_dataset.csv")


print(df.head())


print(df.info())


print(df.describe())


df = df.dropna()  


df['Date'] = pd.to_datetime(df['Date'])


weather = df[['Date', 'Temp', 'Humidity', 'Rainfall']]

weather = pd.read_csv("python/weather_dataset.csv")


mean_temp = np.mean(weather['Temp'])
max_temp = np.max(weather['Temp'])
min_humidity = np.min(weather['Humidity'])
std_rainfall = np.std(weather['Rainfall'])

print('Mean Temp:', mean_temp)
print('Max Temp:', max_temp)
print('Min Humidity:', min_humidity)
print('Std Rainfall:', std_rainfall)

weather = pd.read_csv("python/weather_dataset.csv")
plt.plot(weather['Date'], weather['Temp'])
plt.title('Daily Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.savefig('temp_trend.png')
plt.show()

monthly_rainfall = weather.groupby(weather['Date'].dt.month)['Rainfall'].sum()
monthly_rainfall.plot(kind='bar')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.savefig('monthly_rainfall.png')
plt.show()

plt.scatter(weather['Temp'], weather['Humidity'])
plt.title('Humidity vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.savefig('humidity_temp_scatter.png')
plt.show()
