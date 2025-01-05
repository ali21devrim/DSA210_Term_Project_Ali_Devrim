##Code to create a line chart showing daily air temperature:##

import pandas as pd
import matplotlib.pyplot as plt

# Upload Excel file
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"  # Dosya yolunu güncellediğiniz yer
weather_data = pd.read_excel(file_path)

# Convert date column to datetime format
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Editing the temperature column (clearing the degree symbol and converting it to a number)
weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)

# Calculating the average of temperatures
average_temperature = weather_data['Temperature'].mean()

# Temperature change graph over time
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'], color='orange', marker='o', linestyle='-', linewidth=2, label='Daily Temperature')

# Adding an average line
plt.axhline(y=average_temperature, color='red', linestyle='--', linewidth=1.5, label=f'Average ({average_temperature:.2f}°C)')

# Chart labels and title
plt.title("Temperature Over Time with Average Line", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Graphics editing
plt.tight_layout()
plt.show()
