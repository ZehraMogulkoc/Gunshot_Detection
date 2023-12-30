Gunshot Detection Using CNN
Overview
This repository focuses on the development and deployment of a gunshot detection system powered by Convolutional Neural Networks (CNNs). The core model architecture and training procedures are meticulously detailed in the prediction_model.ipynb notebook.

Model Architecture
The constructed model employs a series of convolutional layers designed to extract intricate spatial features from audio data. Here's a breakdown of the model architecture:

Convolutional Layers: The network starts with 16 filters in the initial layer, subsequently doubling the filter count in the following layers (32, 64, and 128). Each Conv2D layer uses a 2x2 kernel size and a 'same' padding strategy, ensuring feature extraction from the input audio spectrograms.

Pooling Layers: Each convolutional layer is followed by a MaxPooling2D layer with a pool size of 1, effectively reducing spatial dimensions and enhancing computational efficiency.

Dropout Layers: Incorporated between the convolutional layers, Dropout layers with a rate of 0.2 serve as regularization mechanisms, preventing overfitting by randomly deactivating a portion of the neurons during training.

GlobalAveragePooling2D: Positioned at the end of the network, this layer performs global average pooling on the spatial dimensions, consolidating features and reducing the model's parameter count.

Dense Layer: The final layer is a fully connected Dense layer with a sigmoid activation function, suitable for binary classification tasks. Ensure num_labels is appropriately set for the desired classification outcome.

Dataset Augmentation
To bolster the efficacy and accuracy of our detection model, we enriched the renowned Urban8K dataset with an additional 900 gunshot sound samples. This augmentation strategy facilitated the creation of a binary dataset, enabling the model to distinguish between gunshot and ambient sounds effectively.

Key Highlights
Enhanced Dataset: Integration of 900 additional gunshot samples into the Urban8K dataset, refining model performance.
Optimized CNN Model: A meticulously designed CNN architecture tailored for high-precision gunshot detection tasks.
Binary Classification: The model is configured for binary classification, adeptly identifying gunshot sounds amidst varying environmental noises.
Future Prospects
While the existing model showcases promising results, ongoing efforts are directed toward refining the architecture, optimizing hyperparameters, and further expanding the dataset to enhance detection capabilities.
