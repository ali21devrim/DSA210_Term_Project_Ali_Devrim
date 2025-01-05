import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"  # Dosya yolunu güncellediğiniz yer
weather_data = pd.read_excel(file_path)

# Tarih sütununu datetime formatına çevirme
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Sıcaklık sütununu düzenleme (Derece sembolünü temizleme ve sayıya çevirme)
weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)

# Sıcaklıkların ortalamasını hesaplama
average_temperature = weather_data['Temperature'].mean()

# Sıcaklık zamanla değişim grafiği
plt.figure(figsize=(12, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'], color='orange', marker='o', linestyle='-', linewidth=2, label='Daily Temperature')

# Ortalama çizgisi ekleme
plt.axhline(y=average_temperature, color='red', linestyle='--', linewidth=1.5, label=f'Average ({average_temperature:.2f}°C)')

# Grafik etiketleri ve başlık
plt.title("Temperature Over Time with Average Line", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right')

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
