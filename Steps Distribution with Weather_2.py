import pandas as pd
import matplotlib.pyplot as plt

# Hava durumu ve adım sayıları dosyalarının yolları
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Hava durumu verilerini okuma
weather_data = pd.read_excel(weather_file_path)
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

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

# Medyan değerlerini hesaplama
median_values = merged_data.groupby('Weather')['Steps'].median()

# Hava durumu türlerine göre adım sayısı dağılımını görselleştirme
plt.figure(figsize=(12, 6))
merged_data.boxplot(column='Steps', by='Weather', grid=False, patch_artist=True,
                    boxprops=dict(facecolor='lightblue', color='blue'))

# Ortalama çizgisi ekleme
plt.axhline(y=10917, color='red', linestyle='--', label='Overall Average')

# Medyan değerlerini gösterme
for i, weather in enumerate(median_values.index, start=1):
    plt.text(i, median_values[weather], f"{median_values[weather]:.0f}",
             horizontalalignment='center', color='black', fontsize=10)

# Grafik etiketleri ve başlık
plt.title("Steps Distribution by Weather", fontsize=16)
plt.suptitle("")  # Otomatik üst başlığı kaldırır
plt.xlabel("Weather Type", fontsize=12)
plt.ylabel("Steps", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend()

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
