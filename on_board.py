# Required Imports
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import requests
import librosa

# Define the recording upload URL of your Flask application
RECORDING_UPLOAD_URL = 'http://127.0.0.1:5000'

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="D:\\iot_project\\model.tflite")
interpreter.allocate_tensors()

# Define classes
classes = ["no_gun_shot", "gun_shot"]

def load_features():
    #model.load_weights(weights_path)
    backup = pd.HDFStore('Backups//dataframes_backup.h5', 'r+')
    featuresdf = backup["featuresdf"]
    backup.close()
    return featuresdf

featuresdf = load_features()

# Convert features and corresponding classification labels into numpy arrays
X = np.array(featuresdf.feature.tolist())
y = np.array(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y))

# Split the dataset
num_rows = 4
num_columns = 10
num_channels = 1
x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.01, random_state=42)
x_train = x_train.reshape(x_train.shape[0], num_rows, num_columns, num_channels)
x_test = x_test.reshape(x_test.shape[0], num_rows, num_columns, num_channels)

# Define input shape
input_shape = (1, x_train.shape[1], x_train.shape[2], x_train.shape[3])

def predict_class(featuresdf):
    input_data = featuresdf.reshape(input_shape).astype(np.float32)
    input_details = interpreter.get_input_details()
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_details = interpreter.get_output_details()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    pred_index = np.argmax(output_data, axis=1)[0]
    pred_class = classes[pred_index]
    return pred_index, pred_class

def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40, n_mels=40, n_fft=1103)
        mfccs_mean = np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error encountered while processing file: {file_path}. Error: {e}")
        return None
    return mfccs_mean

def main(selected_files):
    no_of_gunshots = 0
    no_of_not_gunshots = 0

    for i, file in enumerate(selected_files):
        print("Making prediction on file " + str(i) + ": " + file.split("/")[-1])
        f_features3 = extract_features(file)
        
        if f_features3 is not None:
            class_index, class_name = predict_class(f_features3)
            print("\tPredicted Class Name: " + str(class_name))
            
            if "gun_shot" == class_name:
                no_of_gunshots += 1
                print("Gunshot detected.")
                """
                in this part it should connect to the web 
                with open(file, 'rb') as f:
                    files = {'file': f}
                    response = requests.post(RECORDING_UPLOAD_URL, files=files)
                    
                if response.status_code == 200:
                    print("Recording uploaded to Flask application successfully.")
                else:
                    print("Failed to upload recording to Flask application. Status code:", response.status_code)
                """
            else:
                no_of_not_gunshots += 1

    print("No. of gun_shots:", no_of_gunshots)
    print("No. of not_gunshots:", no_of_not_gunshots)

# Example usage with file paths
selected_files = [r"D:\iot_project\Fold_increased\audio\fold26\66601-8-0-3.wav"]  # Replace with your file paths
main(selected_files)
