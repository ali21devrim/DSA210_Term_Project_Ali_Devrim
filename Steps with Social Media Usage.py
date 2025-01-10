#This code writes social media usage in minutes on the y-axis and writes the number of daily steps taken on the x-axis. It draws a regression line between the two values, 
#allowing you to understand the relationship between them.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Finding files
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"
social_media_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Ekran Süresi Dataları.xlsx"

# Reading step count data from file
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            date = pd.to_datetime(parts[0].split(": ")[1])
            steps = int(parts[1].split(": ")[1])
            steps_data.append({'Date': date, 'Steps': steps})
steps_df = pd.DataFrame(steps_data)

# Reading social media usage data from file
social_media_data = pd.read_excel(social_media_file_path)
social_media_data['Date'] = pd.to_datetime(social_media_data['Date'])

# Calculating total social media usage time
social_media_data['Total_Social_Media_Usage'] = social_media_data.iloc[:, 1:].sum(axis=1)

# # Combining step count and social media data
merged_data = pd.merge(steps_df, social_media_data[['Date', 'Total_Social_Media_Usage']], on='Date', how='inner')

# Scatter plot and linear regression line
plt.figure(figsize=(10, 6))
plt.scatter(merged_data["Steps"], merged_data["Total_Social_Media_Usage"], label="Data Points", alpha=0.7, color='blue')
plt.title("Relationship Between Social Media Usage and Steps")
plt.xlabel("Steps")
plt.ylabel("Social Media Usage (Minutes)")

# Adding a linear regression line
slope, intercept = np.polyfit(merged_data["Steps"], merged_data["Total_Social_Media_Usage"], 1)
regression_line = slope * merged_data["Steps"] + intercept
plt.plot(merged_data["Steps"], regression_line, color="red", label="Regression Line")

# Editing the chart
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show chart
plt.show()
