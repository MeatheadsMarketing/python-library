import tensorflow as tf
from tensorflow import keras

def build_dense_model(input_shape):
    """Creates a simple fully connected neural network model."""
    model = keras.Sequential([
        keras.layers.Dense(64, activation="relu", input_shape=(input_shape,)),
        keras.layers.Dense(32, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid")
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model
