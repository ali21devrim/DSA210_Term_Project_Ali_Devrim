import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Tarih sütununu düzenleme ve haftanın günlerini ekleme
social_media_data['Date'] = pd.to_datetime(social_media_data['Date'])
social_media_data['Weekday'] = social_media_data['Date'].dt.day_name()

# Total sütununu kontrol etme
if "Total" in social_media_data.columns:
    # Haftanın her günü için ortalama kullanım sürelerini hesaplama
    weekly_averages = social_media_data.groupby('Weekday')['Total'].mean()

    # Gün sırasını koruma (Pazartesi'den Pazar'a)
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_averages = weekly_averages.reindex(ordered_days)

    # Sütun grafiği oluşturma
    plt.figure(figsize=(10, 6))
    weekly_averages.plot(kind='bar', color='skyblue', edgecolor='black')

    # Grafik etiketleri ve başlık
    plt.title('Average Social Media Usage by Weekday')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Usage Time (Minutes)')
    plt.xticks(rotation=45, ha='right')

    # Ortalama çizgisini gösterme
    plt.axhline(y=weekly_averages.mean(), color='red', linestyle='--', linewidth=1.5, label=f'Overall Average ({weekly_averages.mean():.2f} mins)')
    plt.legend()

    # Grafik düzenlemesi
    plt.tight_layout()

    # Grafiği gösterme
    plt.show()
else:
    print("Total sütunu bulunamadı. Lütfen dosyanızı kontrol edin.")
