import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

# Günlük adım sayısı verilerinin bulunduğu dosya yolu
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Günlük adım sayılarını okuma ve haftanın günlerine göre gruplama
weekday_steps = defaultdict(list)

try:
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 2:
                date_str = parts[0].split(": ")[1]
                steps = int(parts[1].split(": ")[1])
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                weekday = date.strftime("%A")  # Haftanın gününü alır
                weekday_steps[weekday].append(steps)

    # Haftanın her günü için ortalama adım sayısını hesaplama
    average_steps_by_weekday = {
        day: sum(steps) / len(steps) for day, steps in weekday_steps.items()
    }

    # Tüm günlerin genel ortalamasını hesaplama
    overall_average = sum(sum(steps) for steps in weekday_steps.values()) / sum(len(steps) for steps in weekday_steps.values())

    # Haftanın günlerini sıralama
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    average_steps_sorted = [average_steps_by_weekday.get(day, 0) for day in ordered_days]

    # Grafiği oluşturma
    plt.figure(figsize=(10, 6))
    plt.bar(ordered_days, average_steps_sorted, color='purple', edgecolor='black', label="Average Steps by Day")

    # Ortalama çizgisi ekleme
    plt.axhline(y=overall_average, color='red', linestyle='--', linewidth=1.5, label=f'Overall Average ({overall_average:.0f})')

    # Grafik etiketleri ve başlık
    plt.title("Average Steps by Weekday with Overall Average Line", fontsize=16)
    plt.xlabel("Day of the Week", fontsize=12)
    plt.ylabel("Average Steps", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Grafik düzenlemesi
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Dosya bulunamadı: {file_path}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
