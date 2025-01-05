import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# XML dosyasını yükleme
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Adım Sayısı-Parsing\Günlük_Adım_Sayısı_Corrected.xml"
tree = ET.parse(file_path)
root = tree.getroot()

# Adım sayısı verilerini saat bazında toplama
hourly_steps = defaultdict(list)

for record in root.findall(".//Record[@type='HKQuantityTypeIdentifierStepCount']"):
    start_date = record.get("startDate")
    value = int(record.get("value"))

    # Başlangıç saatini çıkarma
    hour = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S +0300").strftime("%H")
    hourly_steps[hour].append(value)

# Saatlere göre ortalama adım sayısını hesaplama
average_steps = {hour: sum(values) / len(values) for hour, values in hourly_steps.items()}

# Saatleri ve ortalama adım sayılarını sıralama
sorted_hours = sorted(average_steps.keys())
sorted_average_steps = [average_steps[hour] for hour in sorted_hours]

# Saat bazında ortalama adım sayısı grafiği oluşturma
plt.figure(figsize=(12, 6))
plt.bar(sorted_hours, sorted_average_steps, color='orange', edgecolor='black')

# Grafik etiketleri ve başlık
plt.title("Average Hourly Step Count", fontsize=16)
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Average Steps", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, fontsize=10, ha='right')

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
