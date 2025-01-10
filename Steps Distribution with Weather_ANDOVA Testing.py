import pandas as pd
from scipy.stats import f_oneway

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
merged_data = pd.merge(steps_df, weather_data, on='Date', how='inner')

# Hava durumu türlerine göre gruplandırma ve ANOVA testi
grouped = merged_data.groupby('Weather')['Steps']

# ANOVA testi
anova_result = f_oneway(*[group.values for name, group in grouped])

# Test sonuçlarını yazdırma
threshold = 0.05  # Threshold değeri
print("\nANOVA Testi Sonucu:")
print(f"F-statistic: {anova_result.statistic:.4f}")
print(f"p-value: {anova_result.pvalue:.4f}")

# H0 ve HA Bilgileri
print("\nHipotezler:")
print("H0: Hava durumu adım sayısı üzerinde etkili değildir.")
print("HA: Hava durumu adım sayısı üzerinde etkilidir.")

# p-value ve threshold karşılaştırması
if anova_result.pvalue < threshold:
    print("\nSonuç: H0 reddedilir. Hava durumu, adım sayısı üzerinde etkili olabilir.")
else:
    print("\nSonuç: H0 reddedilemez. Hava durumu, adım sayısı üzerinde anlamlı bir etki göstermiyor.")
