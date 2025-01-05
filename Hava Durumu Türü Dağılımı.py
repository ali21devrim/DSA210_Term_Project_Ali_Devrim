import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
weather_data = pd.read_excel(file_path)

# Tarih sütununu datetime formatına çevirme
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Eğer nem sütununda % işareti varsa kaldırılır
if weather_data['Humidity'].dtype == 'object':
    weather_data['Humidity'] = weather_data['Humidity'].str.replace('%', '').astype(float)

# Nem oranının zamanla değişim grafiği
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Humidity'], color='blue', marker='o', linestyle='-', linewidth=2, label='Daily Humidity')

# Grafik etiketleri ve başlık
plt.title("Daily Humidity Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Humidity (%)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')
plt.legend()

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
