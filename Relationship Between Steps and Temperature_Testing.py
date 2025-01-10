import pandas as pd
from scipy.stats import ttest_ind, normaltest, mannwhitneyu

def test_temperature_steps_relationship(weather_file_path, steps_file_path):
    # Reading weather data
    weather_data = pd.read_excel(weather_file_path)
    weather_data['Date'] = pd.to_datetime(weather_data['Date'])
    weather_data['Temperature'] = weather_data['Temperature'].str.replace('°C', '').astype(float)

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

    # Grouping of data
    steps_above_11 = merged_data[merged_data['Temperature'] > 11]['Steps']
    steps_below_or_equal_11 = merged_data[merged_data['Temperature'] <= 11]['Steps']

    # Hypotheses
    print("\nHipotezler:")
    print("H0: Hava sıcaklığı 11°C üzeri olduğunda günlük ortalama adım sayısı genel ortalamadan farklı değildir.")
    print("HA: Hava sıcaklığı 11°C üzeri olduğunda günlük ortalama adım sayısı genel ortalamadan farklıdır.")

    # Checking whether the data are normally distributed
    normal_above = normaltest(steps_above_11).pvalue
    normal_below = normaltest(steps_below_or_equal_11).pvalue

    print("\nNormal dağılım test sonuçları:")
    print(f"Hava sıcaklığı 11°C üzeri: p-value = {normal_above:.4f}")
    print(f"Hava sıcaklığı 11°C ve altı: p-value = {normal_below:.4f}")

    # Selection of appropriate test
    if normal_above > 0.05 and normal_below > 0.05:
        # Bağımsız örnekleme t-testi
        test_result = ttest_ind(steps_above_11, steps_below_or_equal_11)
        test_name = "Bağımsız Örnekleme t-Testi"
    else:
        # Mann-Whitney U testi
        test_result = mannwhitneyu(steps_above_11, steps_below_or_equal_11, alternative='two-sided')
        test_name = "Mann-Whitney U Testi"

    # Print results
    print(f"\n{test_name} Sonuçları:")
    print(f"Test İstatistiği: {test_result.statistic:.4f}")
    print(f"p-value: {test_result.pvalue:.4f}")

    # Hypothesis testing decision
    threshold = 0.05
    if test_result.pvalue < threshold:
        print("\nSonuç: H0 reddedilir. Hava sıcaklığı 11°C üzeri olduğunda günlük ortalama adım sayısı genel ortalamadan farklıdır.")
    else:
        print("\nSonuç: H0 reddedilemez. Hava sıcaklığı 11°C üzeri olduğunda günlük ortalama adım sayısı genel ortalamadan farklı değildir.")

# File paths
weather_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Hava Durumu Dataları.xlsx"
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"

# Run the function
test_temperature_steps_relationship(weather_file_path, steps_file_path)
