#This code evaluated the daily step count according to the weather conditions rather than the air temperature. For this purpose, three types of weather conditions experienced
#in autumn (clear, partly cloudy and rain) were considered. Candlestick charts were created to determine the distribution of the number of steps taken in these weather
#conditions.

import pandas as pd
import matplotlib.pyplot as plt

# Paths to weather and step count files
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Reading weather data
weather_data = pd.read_excel(weather_file_path)
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

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

# Calculating median values
median_values = merged_data.groupby('Weather')['Steps'].median()

# Visualize step count distribution by weather types
plt.figure(figsize=(12, 6))
merged_data.boxplot(column='Steps', by='Weather', grid=False, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='blue'))

# Adding an average line
plt.axhline(y=10917, color='red', linestyle='--', label='Overall Average')

# Showing median values
for i, weather in enumerate(median_values.index, start=1):
    plt.text(i, median_values[weather], f"{median_values[weather]:.0f}",
             horizontalalignment='center', color='black', fontsize=10)

# Chart labels and title
plt.title("Steps Distribution by Weather", fontsize=16)
plt.suptitle("")  # Otomatik üst başlığı kaldırır
plt.xlabel("Weather Type", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend()

# Graphics editing
plt.tight_layout()
plt.show()
