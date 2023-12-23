import pandas as pd
import os

# Path to UrbanSound8K dataset
urban_sound_path = "D:\\iot_project\\UrbanSound8K"
count=0

# Path to the new gunshot sound files
gunshot_path = "D:\iot_project\oyun"

# Load UrbanSound8K metadata
urban_sound_metadata_path = os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K.csv")
urban_sound_metadata = pd.read_csv(urban_sound_metadata_path)

# Load metadata for new gunshot files
gunshot_metadata = pd.DataFrame({
    'slice_file_name': os.listdir(gunshot_path),
    'fsID': range(len(os.listdir(gunshot_path))),
    'start': 0.0,
    'end': 1.0,
    'salience': 1,
    'fold': 10,  # Assign a new fold number
    'classID': 6,  # Assign a new classID
    'class': 'gun_shot'
})

# Append gunshot metadata to UrbanSound8K metadata
combined_metadata = urban_sound_metadata.append(gunshot_metadata, ignore_index=True)

# Save the combined metadata to a new CSV file
combined_metadata.to_csv(os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K.csv"), index=False)
'''

'''
# Move gunshot audio files to the UrbanSound8K audio directory
for filename in os.listdir(gunshot_path):
    count+=1
    src_path = os.path.join(gunshot_path, filename)
    dst_path = os.path.join(urban_sound_path, "audio/fold1", filename)
    os.rename(src_path, dst_path)

print(count)
