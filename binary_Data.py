import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import os

urban_sound_path = "D:\\iot_project\\Fold_increased"
# Load UrbanSound8K metadata
urban_sound_metadata_path = os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K-modified.csv")
df = pd.read_csv(urban_sound_metadata_path)
#df = pd.DataFrame.from_csv(dataset_csv)
print(df.columns)
print("\nClasses:")
print(set(df["class"]))

folds = len(set(df["fold"]))
print("\nNumber of folds: " + str(folds))

new_metadata = df.copy()
# replace classes which are not gun_shot with no_gun_shot
new_metadata.loc[df["class"] != "gun_shot", "classID"] = 0
new_metadata.loc[df["class"] == "gun_shot", "classID"] = 1
new_metadata.groupby("classID").count()

new_metadata.to_csv(r"D:\iot_project\Fold_increased\metadata\CombinedUrbanSound8K-modified.csv",index=False)
