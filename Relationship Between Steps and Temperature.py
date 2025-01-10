#This code is written to create a chart showing how many steps I took in what temperature. At the same time, the resulting chart shows at what temperature the number of steps
#taken was above average. It is difficult to get an idea from the chart because the points seem to be randomly distributed.

import pandas as pd
import matplotlib.pyplot as plt

# Paths to weather and step count files
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Reading weather data
weather_data = pd.read_excel(weather_file_path)
weather_data['Date'] = pd.to_datetime(weather_data['Date'])
weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)

# Reading step count data
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = pd.to_datetime(parts[0].split(": ")[1])
            steps = int(parts[1].split(": ")[1])
            steps_data.append({'Date': date, 'Steps': steps})

steps_df = pd.DataFrame(steps_data)

# Combining weather and step count data
merged_data = pd.merge(steps_df, weather_data, on='Date')

# Average number of steps
average_steps = merged_data['Steps'].mean()

# Visualizing the relationship between air temperature and step count
plt.figure(figsize=(12, 6))
plt.scatter(merged_data['Temperature'], merged_data['Steps'], color='blue', alpha=0.7, label="Steps")
plt.axhline(average_steps, color='red', linestyle='--', label=f'Average Steps ({int(average_steps)})')

# Chart labels and title
plt.title("Relationship Between Temperature and Steps", fontsize=16)
plt.xlabel("Temperature (°C)", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.legend()
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Graphics editing
plt.tight_layout()
plt.show()
