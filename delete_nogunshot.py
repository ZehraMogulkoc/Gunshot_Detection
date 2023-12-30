import os
import shutil
import random

# Define directories
base_audio_dir = r".\Fold_increased\audio"
new_audio_dir = r".\Fold_increased\undersampled_audio"

# Create a directory for undersampled audio files if it doesn't exist
if not os.path.exists(new_audio_dir):
    os.makedirs(new_audio_dir)

# Iterate through each fold directory
for fold in os.listdir(base_audio_dir):
    fold_dir = os.path.join(base_audio_dir, fold)
    
    # Create a corresponding directory in the new location
    new_fold_dir = os.path.join(new_audio_dir, fold)
    if not os.path.exists(new_fold_dir):
        os.makedirs(new_fold_dir)

    # List all audio files in the current fold directory
    audio_files = [f for f in os.listdir(fold_dir) if f.endswith('.wav')]

    # Shuffle the list of audio files for randomness
    random.shuffle(audio_files)

    # Calculate the number of instances in the minority class (gun_shot)
    num_gunshots = 1245  # Based on your data

    # Undersample the majority class (no_gun_shot) to match the number of gun_shot instances
    undersampled_files = [f for f in audio_files if "no_gun_shot" in f][:6000]

    # Copy undersampled audio files to the new directory for the current fold
    for file in undersampled_files:
        src_path = os.path.join(fold_dir, file)
        dst_path = os.path.join(new_fold_dir, file)
        shutil.copy(src_path, dst_path)
