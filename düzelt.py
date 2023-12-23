import pandas as pd
import os


# Path to the UrbanSound8K dataset
urban_sound_path = "D:\\iot_project\\UrbanSound8K"

# Path to save the updated CSV file
updated_metadata_path = os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K.csv")

# Load UrbanSound8K metadata
urban_sound_metadata_path = os.path.join(urban_sound_path, "metadata", "CombinedUrbanSound8K.csv")
urban_sound_metadata = pd.read_csv(urban_sound_metadata_path)

# Update the 'fold' column where 'slice_file_name' starts with '8 ('
urban_sound_metadata.loc[urban_sound_metadata['slice_file_name'].str.startswith('3 ('), 'fold'] = 10

# Display the updated DataFrame
print(urban_sound_metadata)

# Save the updated DataFrame to a new CSV file
urban_sound_metadata.to_csv(updated_metadata_path, index=False)  # Setting index=False avoids writing row indices to the CSV
