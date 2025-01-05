##**Here is the code for the line chart that shows how many steps I take per day:**##

import matplotlib.pyplot as plt

# Güncellenmiş dosya yolu
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Günlük adım sayılarını listeye aktarma
daily_steps = []
with open(file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = parts[0].split(": ")[1]
            steps = int(parts[1].split(": ")[1])
            daily_steps.append({"Date": date, "Steps": steps})

# Verileri grafiğe hazırlama
dates = [entry["Date"] for entry in daily_steps]
steps = [entry["Steps"] for entry in daily_steps]

# Ortalama adım sayısını hesaplama
average_steps = sum(steps) / len(steps)

# Günlük adım sayısı grafiği oluşturma
plt.figure(figsize=(12, 6))
plt.plot(dates, steps, color='blue', marker='o', linestyle='-', linewidth=2, label='Daily Steps')

# Ortalama çizgisi ekleme
plt.axhline(y=average_steps, color='red', linestyle='--', linewidth=1.5, label=f'Average Steps ({average_steps:.0f})')

# Grafik etiketleri ve başlık
plt.title("Daily Step Count Over Time with Average Line", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Steps", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.legend()

# Grafik düzenlemesi
plt.tight_layout()
plt.show()
