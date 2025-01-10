#I wrote this code to create a bar chart that shows which days I use social media the most, and which days are above average. It's not surprising that the weekends are above
average, but it's surprising that Monday, my least busy weekday, is the day with the lowest average.#

import pandas as pd
import matplotlib.pyplot as plt

# Uploading Excel file
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Edit the date column and add days of the week
social_media_data['Date'] = pd.to_datetime(social_media_data['Date'])
social_media_data['Weekday'] = social_media_data['Date'].dt.day_name()

# Checking the Total column
if "Total" in social_media_data.columns:
    # Haftanın her günü için ortalama kullanım sürelerini hesaplama
    weekly_averages = social_media_data.groupby('Weekday')['Total'].mean()

    # Maintaining the order of the day (Monday to Sunday)
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_averages = weekly_averages.reindex(ordered_days)

    # Create a column chart
    plt.figure(figsize=(10, 6))
    weekly_averages.plot(kind='bar', color='skyblue', edgecolor='black')

    # Chart labels and title
    plt.title('Average Social Media Usage by Weekday')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Usage Time (Minutes)')
    plt.xticks(rotation=45, ha='right')

    # Show average line
    plt.axhline(y=weekly_averages.mean(), color='red', linestyle='--', linewidth=1.5, label=f'Overall Average ({weekly_averages.mean():.2f} mins)')
    plt.legend()

    # Graphics editing
    plt.tight_layout()

    # Show chart
    plt.show()
