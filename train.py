import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv1D, MaxPooling1D
import pickle
import time
import numpy as np


pickle_in = open("X.pickle","rb")
X_train = pickle.load(pickle_in)
for idx, x in enumerate(X_train):
    if len(x) < 8000:
        X_train[idx] = np.pad(x, (0, 8000-len(x)))

pickle_in = open("y.pickle","rb")
y_train = pickle.load(pickle_in)

X_train = tf.convert_to_tensor(X_train)
X_train = tf.expand_dims(X_train, 2)
y_train = tf.convert_to_tensor(y_train)

model = Sequential()
model.add(Conv1D(8, 13, activation="relu", input_shape=(8000, 1), padding="valid", strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))
model.add(Conv1D(16, 11, activation="relu", padding="valid", strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))
model.add(Conv1D(32 ,9, activation="relu", padding="valid", strides=1))
model.add(MaxPooling1D(3))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(12, activation="softmax"))

model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              optimizer=tf.keras.optimizers.Nadam(),
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=100, validation_split=0.15,shuffle=True)

model.save("speech_model")

time.sleep(1)


# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model('speech_model')  # path to the SavedModel directory
tflite_model = converter.convert()

# Save the lite model
with open('RaspberryPi/speech_model.tflite', 'wb') as f:
    f.write(tflite_model)
