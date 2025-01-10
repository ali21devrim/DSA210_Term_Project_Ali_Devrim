import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Platformların günlük ortalama sürelerini hesaplama
platforms = ["TikTok", "Instagram", "Twitter (X)", "Youtube"]
average_durations = social_media_data[platforms].mean()

# Grafik oluşturma
plt.figure(figsize=(10, 6))
average_durations.plot(kind='bar', color=['black', 'red', 'blue', 'gray'], edgecolor='black')

# Grafik etiketleri ve başlık
plt.title("Average Daily Social Media Usage by Platform")
plt.xlabel("Social Media Platform")
plt.ylabel("Average Usage Time (Minutes)")
plt.xticks(rotation=0)  # X ekseni etiketlerini yatay tut

# Grafik düzenlemesi
plt.tight_layout()

# Grafiği gösterme
plt.show()
