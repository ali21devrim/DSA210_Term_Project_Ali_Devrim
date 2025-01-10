import pandas as pd
import matplotlib.pyplot as plt

# Hava durumu ve adım sayıları dosyalarının yolları
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Hava durumu verilerini okuma
weather_data = pd.read_excel(weather_file_path)
weather_data['Date'] = pd.to_datetime(weather_data['Date'])
weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)

# Adım sayısı verilerini okuma
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = pd.to_datetime(parts[0].split(": ")[1])
            steps = int(parts[1].split(": ")[1])
            steps_data.append({'Date': date, 'Steps': steps})

steps_df = pd.DataFrame(steps_data)

# Hava durumu ve adım sayısı verilerini birleştirme
merged_data = pd.merge(steps_df, weather_data, on='Date')

# Ortalama adım sayısı
average_steps = merged_data['Steps'].mean()

# Hava sıcaklığı ile adım sayısı ilişkisini görselleştirme
plt.figure(figsize=(12, 6))
plt.scatter(merged_data['Temperature'], merged_data['Steps'], color='blue', alpha=0.7, label="Steps")
plt.axhline(average_steps, color='red', linestyle='--', label=f'Average Steps ({int(average_steps)})')

# Grafik etiketleri ve başlık
plt.title("Relationship Between Temperature and Steps", fontsize=16)
plt.xlabel("Temperature (°C)", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.legend()
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
