
"""
import pandas as pd

data_set = pd.read_csv("abalone.csv")
print(data_set.head())
print(data_set.shape)
"""
from platform import python_version
print(python_version())

"""
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# 1. Load and Preprocess Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to [0, 1] range
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape to add a channel dimension (for grayscale images)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# 2. Build the Model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes for digits 0–9
])

# 3. Compile the Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Train the Model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# 5. Evaluate the Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc}")

# 6. Make Predictions
predictions = model.predict(x_test)

# Example: Visualize a prediction
import numpy as np
index = 0  # Change to see different test images
plt.imshow(x_test[index].reshape(28, 28), cmap='gray')
plt.title(f"Predicted Label: {np.argmax(predictions[index])}")
plt.show()
"""
