import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather_dataset.csv")

print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")

df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])
weather = df[['Date', 'Temp', 'Humidity', 'Rainfall']]

mean_temp = weather['Temp'].mean()
max_temp = weather['Temp'].max()
min_humidity = weather['Humidity'].min()
std_rainfall = weather['Rainfall'].std()

print("Mean Temp:", mean_temp)
print("Max Temp:", max_temp)
print("Min Humidity:", min_humidity)
print("Std Rainfall:", std_rainfall, "\n")

weather.to_csv("cleaned_weather.csv", index=False)

plt.figure(figsize=(9,4))
plt.plot(weather['Date'], weather['Temp'], marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temp_trend.png")
plt.show()

weather['Month'] = weather['Date'].dt.month
monthly_rainfall = weather.groupby("Month")['Rainfall'].sum()

plt.figure(figsize=(7,4))
monthly_rainfall.plot(kind='bar')
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("monthly_rainfall.png")
plt.show()

plt.figure(figsize=(7,4))
plt.scatter(weather['Temp'], weather['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("humidity_vs_temp.png")
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(11,4))
ax[0].plot(weather['Date'], weather['Temp'])
ax[0].set_title("Temperature Trend")
ax[1].scatter(weather['Temp'], weather['Humidity'])
ax[1].set_title("Temp vs Humidity")
plt.tight_layout()
plt.savefig("combined_plot.png")
plt.show()

