import os
import pandas as pd
import numpy as np
from shutil import copyfile

# Paths
dataset_csv_path = r"D:\iot_project\UrbanSound8K\metadata\CombinedUrbanSound8K.csv"
audio_dir = r"D:\iot_project\UrbanSound8K\audio"
new_dataset_path = r"D:\iot_project\Fold_increased\audio"


# Read the existing CSV file
df = pd.read_csv(dataset_csv_path)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Determine the total number of files and the new files per fold
total_files = len(df)
num_of_folds = 25
files_per_fold = total_files // num_of_folds

# Create the directory structure and copy files
for _, row in df.iterrows():
    curr_fold = (_ // files_per_fold) + 1  # Determine the current fold
    folder_path = os.path.join(new_dataset_path, f"fold{curr_fold}")
    
    # Create directory if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define paths
    original_file_path = os.path.join(audio_dir, f"fold{row['fold']}", row['slice_file_name'])
    new_file_path = os.path.join(folder_path, row['slice_file_name'])
    
    # Check if file exists and then copy
    if os.path.exists(original_file_path):
       # copyfile(original_file_path, new_file_path)
        print(1)
    else:
        print(f"File not found: {original_file_path}")

    # Update fold information
    df.at[_, 'fold'] = curr_fold

# Save the updated metadata to a new CSV file
updated_csv_path = r"D:\iot_project\Fold_increased\metadata\CombinedUrbanSound8K-modified.csv"
df.to_csv(updated_csv_path, index=False)
