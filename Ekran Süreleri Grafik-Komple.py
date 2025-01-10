import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Tarih sütununu düzenleme (sadece tarih kısmını alma)
social_media_data['Date'] = pd.to_datetime(social_media_data['Date']).dt.date

# Günlük ortalamayı hesaplama (Total sütununa göre)
average_total_usage = social_media_data["Total"].mean()

# Grafik oluşturma
social_media_data.set_index('Date', inplace=True)
social_media_data.drop(columns=["Total"], inplace=True)  # "Total" sütununu görselden kaldırıyoruz

# Stacked bar plot
ax = social_media_data.plot(kind='bar', stacked=True, figsize=(12, 6))

# Ortalama çizgisini ekleme
plt.axhline(y=average_total_usage, color='red', linestyle='--', linewidth=1.5, label=f'Average ({average_total_usage:.2f} mins)')

# Grafik etiketleri ve başlık
plt.title('Daily Social Media Usage by Application with Average Line')
plt.xlabel('Date')
plt.ylabel('Usage Time (Minutes)')
plt.legend(title="Applications + Average", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')  # X ekseni etiketlerini döndürme

# Grafik düzenlemesi
plt.tight_layout()

# Grafiği gösterme
plt.show()