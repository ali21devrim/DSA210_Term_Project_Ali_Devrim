**This python code was written to show which application I use for how many minutes per day on average. The result is depicted as bar graphs.**
                                                                                                                              
import pandas as pd
import matplotlib.pyplot as plt

# Upload Excel files
file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\CS210 Project\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(file_path)

# Calculating daily average times of platforms
platforms = ["TikTok", "Instagram", "Twitter (X)", "Youtube"]
average_durations = social_media_data[platforms].mean()

# Creating a chart
plt.figure(figsize=(10, 6))
average_durations.plot(kind='bar', color=['black', 'red', 'blue', 'gray'], edgecolor='black')

# Chart labels and title
plt.title("Average Daily Social Media Usage by Platform")
plt.xlabel("Social Media Platform")
plt.ylabel("Average Usage Time (Minutes)")
plt.xticks(rotation=0)  # X ekseni etiketlerini yatay tut

# Graphics editing
plt.tight_layout()

# Show the graph
plt.show()
