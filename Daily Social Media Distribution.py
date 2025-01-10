#This daily social media usage is a code that determines how much social media I use on each day by displaying different social media platforms in different colors. Before
#analyzing it, I would not have guessed that I use TikTok so much. I thought that the social media platform I use the most is Instagram.

import pandas as pd
import matplotlib.pyplot as plt

# Upload Excel file
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Editing the date column
social_media_data['Date'] = pd.to_datetime(social_media_data['Date']).dt.date

# Calculating daily average
average_total_usage = social_media_data["Total"].mean()

# Creating a chart
social_media_data.set_index('Date', inplace=True)
social_media_data.drop(columns=["Total"], inplace=True)  # "Total" sütununu görselden kaldırıyoruz

# Stacked bar plot
ax = social_media_data.plot(kind='bar', stacked=True, figsize=(12, 6))

# Adding the average line
plt.axhline(y=average_total_usage, color='red', linestyle='--', linewidth=1.5, label=f'Average ({average_total_usage:.2f} mins)')

# Chart labels and title
plt.title('Daily Social Media Usage by Application with Average Line')
plt.xlabel('Date')
plt.ylabel('Usage Time (Minutes)')
plt.legend(title="Applications + Average", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')  # X ekseni etiketlerini döndürme

# Graphics editing
plt.tight_layout()

# Show chart
plt.show()
