##Code that creates the pie chart showing what the weather is like:##

import pandas as pd
import matplotlib.pyplot as plt

# Upload Excel file
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
weather_data = pd.read_excel(file_path)

# Convert date column to datetime format
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# If there is a % sign in the humidity column, it is removed.
if weather_data['Humidity'].dtype == 'object':
    weather_data['Humidity'] = weather_data['Humidity'].str.replace('%', '').astype(float)

# Graph of humidity rate change over time
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Humidity'], color='blue', marker='o', linestyle='-', linewidth=2, label='Daily Humidity')

# Chart labels and title
plt.title("Daily Humidity Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Humidity (%)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.legend()

# Graphics editing
plt.tight_layout()
plt.show()
