import matplotlib.pyplot as plt
import datetime
from collections import defaultdict

# Günlük adım sayısı verilerinin bulunduğu dosya yolu
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Günlük adım sayılarını okuma ve haftalık bazda gruplama
weekly_steps = defaultdict(int)

try:
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 2:
                date_str = parts[0].split(": ")[1]
                steps = int(parts[1].split(": ")[1])
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                week = date.strftime("%Y-W%U")  # Haftalık bazda gruplama (Yıl-Hafta numarası)
                weekly_steps[week] += steps

    # Haftaları ve toplam adım sayılarını sıralama
    sorted_weeks = sorted(weekly_steps.keys())
    sorted_weekly_steps = [weekly_steps[week] for week in sorted_weeks]

    # Grafiği oluşturma
    plt.figure(figsize=(12, 6))
    plt.plot(sorted_weeks, sorted_weekly_steps, color='green', marker='o', linestyle='-', linewidth=2, label='Weekly Steps')

    # Grafik etiketleri ve başlık
    plt.title("Weekly Step Count Trend", fontsize=16)
    plt.xlabel("Week", fontsize=12)
    plt.ylabel("Total Steps", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, fontsize=8, ha='right')
    plt.legend()

    # Grafik düzenlemesi
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Dosya bulunamadı: {file_path}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
