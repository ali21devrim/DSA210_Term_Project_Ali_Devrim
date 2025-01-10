#This code was written after it was determined that the air temperature had no effect on the daily step count. Its purpose was to understand whether the weather had an effect.
#In other words, whether the weather was cloudy, sunny or rainy, this question was tested with an ANOVA test.

import pandas as pd
from scipy.stats import f_oneway

# Paths to weather and step count files
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Reading weather data
weather_data = pd.read_excel(weather_file_path)
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# Reading step count data
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = pd.to_datetime(parts[0].split(": ")[1])
            steps = int(parts[1].split(": ")[1])
            steps_data.append({'Date': date, 'Steps': steps})

steps_df = pd.DataFrame(steps_data)

# Combining weather and step count data
merged_data = pd.merge(steps_df, weather_data, on='Date', how='inner')

# Grouping by weather types and ANOVA test
grouped = merged_data.groupby('Weather')['Steps']

# ANOVA testing
anova_result = f_oneway(*[group.values for name, group in grouped])

# Printing test results
threshold = 0.05  # Threshold değeri
print("\nANOVA Testi Sonucu:")
print(f"F-statistic: {anova_result.statistic:.4f}")
print(f"p-value: {anova_result.pvalue:.4f}")

# H0 and HA Information
print("\nHipotezler:")
print("H0: Hava durumu adım sayısı üzerinde etkili değildir.")
print("HA: Hava durumu adım sayısı üzerinde etkilidir.")

# Comparison of p-value and threshold
if anova_result.pvalue < threshold:
    print("\nConclusion: H0 is rejected. Weather can have an effect on step count.")
else:
    print("\n"Conclusion: H0 cannot be rejected. Weather does not have a significant effect on step count.")
