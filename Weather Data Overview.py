##Below is the code written to create a graph that shows daily humidity percentage and wind speed in addition to temperature information.##

import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
weather_data = pd.read_excel(file_path)

# Tarih sütununu datetime formatına çevirme
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Nem sütununu düzenleme
if weather_data['Humidity'].dtype == 'object':
    weather_data['Humidity'] = weather_data['Humidity'].str.replace('%', '').astype(float)
else:
    weather_data['Humidity'] = weather_data['Humidity'].astype(float)

# Sıcaklık sütununu düzenleme
if weather_data['Temperature'].dtype == 'object':
    weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)
else:
    weather_data['Temperature'] = weather_data['Temperature'].astype(float)

# Rüzgar hızı sütununu düzenleme
if weather_data['Wind Speed'].dtype == 'object':
    weather_data['Wind Speed'] = (
        weather_data['Wind Speed']
        .str.replace(' km/h', '', regex=False)
        .str.replace(' km\\h', '', regex=False)
        .astype(float)
    )
else:
    weather_data['Wind Speed'] = weather_data['Wind Speed'].astype(float)

# Kombine grafik oluşturma
fig, ax1 = plt.subplots(figsize=(14, 8))

# Sıcaklık çizgisi (Y Ekseni 1)
ax1.plot(weather_data['Date'], weather_data['Temperature'], color='orange', marker='o', linestyle='-', label='Temperature (°C)')
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Temperature (°C)', color='orange', fontsize=12)
ax1.tick_params(axis='y', labelcolor='orange')

# Y Ekseni 2 (Nem)
ax2 = ax1.twinx()
ax2.plot(weather_data['Date'], weather_data['Humidity'], color='blue', marker='o', linestyle='-', label='Humidity (%)')
ax2.set_ylabel('Humidity (%)', color='blue', fontsize=12)
ax2.tick_params(axis='y', labelcolor='blue')

# Y Ekseni 3 (Rüzgar Hızı)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Üçüncü y eksenini kaydırma
ax3.plot(weather_data['Date'], weather_data['Wind Speed'], color='green', marker='o', linestyle='-', label='Wind Speed (km/h)')
ax3.set_ylabel('Wind Speed (km/h)', color='green', fontsize=12)
ax3.tick_params(axis='y', labelcolor='green')

# Başlık ve genel düzenleme
plt.title('Weather Data Overview', fontsize=16)
fig.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Gösterge ekleme
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Grafiği gösterme
plt.show()
