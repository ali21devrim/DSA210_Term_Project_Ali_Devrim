import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dosya yolları
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"
social_media_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Ekran Süresi Dataları.xlsx"

# Adım sayısı verilerini dosyadan okuma
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = pd.to_datetime(parts[0].split(": ")[1])
            steps = int(parts[1].split(": ")[1])
            steps_data.append({'Date': date, 'Steps': steps})
steps_df = pd.DataFrame(steps_data)

# Sosyal medya kullanım verilerini dosyadan okuma
social_media_data = pd.read_excel(social_media_file_path)
social_media_data['Date'] = pd.to_datetime(social_media_data['Date'])

# Sosyal medya toplam kullanım süresini hesaplama
social_media_data['Total_Social_Media_Usage'] = social_media_data.iloc[:, 1:].sum(axis=1)

# Adım sayısı ve sosyal medya verilerini birleştirme
merged_data = pd.merge(steps_df, social_media_data[['Date', 'Total_Social_Media_Usage']], on='Date', how='inner')

# Scatter plot ve doğrusal regresyon çizgisi
plt.figure(figsize=(10, 6))
plt.scatter(merged_data["Steps"], merged_data["Total_Social_Media_Usage"], label="Data Points", alpha=0.7, color='blue')
plt.title("Relationship Between Social Media Usage and Steps")
plt.xlabel("Steps")
plt.ylabel("Social Media Usage (Minutes)")

# Doğrusal regresyon çizgisi ekleme
slope, intercept = np.polyfit(merged_data["Steps"], merged_data["Total_Social_Media_Usage"], 1)
regression_line = slope * merged_data["Steps"] + intercept
plt.plot(merged_data["Steps"], regression_line, color="red", label="Regression Line")

# Grafiği düzenleme
plt.legend()
plt.grid(True)
plt.tight_layout()

# Grafiği gösterme
plt.show()
