import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os


urban_sound_path = "D:\\iot_project\\UrbanSound8K"

# Load UrbanSound8K metadata
urban_sound_metadata_path = os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K-2.csv")
df = pd.read_csv(urban_sound_metadata_path)

print(df.columns)
print("\nClasses:")
print(set(df["class"]))

# Determine the number of unique folds
folds = len(set(df["fold"]))
print("\nNumber of folds: " + str(folds))

# Create a copy of the dataframe for modifications
new_metadata = df.copy()

# Update the 'class' column based on the 'classID' column
new_metadata.loc[df["classID"] == 1, "class"] = "gun_shot"
new_metadata.loc[df["classID"] == 0, "class"] = "no_gun_shot"

# Group by the 'class' to see the count in each category
print(new_metadata.groupby("class").count())

# Save the updated metadata to a new CSV file
new_metadata.to_csv(r"D:\iot_project\UrbanSound8K\metadata\CombinedUrbanSound8K-2.csv", index=False)
