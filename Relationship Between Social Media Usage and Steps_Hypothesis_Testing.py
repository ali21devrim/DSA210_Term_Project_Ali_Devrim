import pandas as pd
from scipy.stats import spearmanr

# Load the steps data
steps_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\daily_steps_output.txt"
steps_data = []
with open(steps_file_path, "r") as file:
    for line in file:
        date, steps = line.strip().split(", ")
        steps = int(steps.split(": ")[1])
        steps_data.append(steps)

# Load social media data
social_media_file_path = r"C:\Users\alide\OneDrive - sabanciuniv.edu\Masaüstü\Ekran Süresi Dataları.xlsx"
social_media_data = pd.read_excel(social_media_file_path)

# Ensure both datasets have the same length and align
min_length = min(len(steps_data), len(social_media_data))
steps_data = steps_data[:min_length]
social_media_data = social_media_data.iloc[:min_length]

# Display the hypotheses
print("Hypotheses:")
print("H0: Step count increase does not significantly reduce social media usage.")
print("HA: Step count increase significantly reduces social media usage.\n")

# Calculate Spearman correlation coefficient
correlation, p_value = spearmanr(steps_data, social_media_data['Total'])

# Display results
print("Hypothesis Testing Results:")
print(f"Spearman Correlation Coefficient: {correlation:.4f}")
print(f"P-Value: {p_value:.4f}")

# Hypothesis outcome
threshold = 0.05
print("\nConclusion:")
if p_value < threshold:
    print("Reject the null hypothesis (H0): There is a significant relationship between step count and social media usage.")
else:
    print("Fail to reject the null hypothesis (H0): There is no significant relationship between step count and social media usage.")

