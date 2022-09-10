"""
Script for preprocessing of the dataset
Before execution, download data from
https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data
and put desired files sorted by categories into folder 'training'_data'.
I used the following 12 categories:
'yes'
'no'
'zero'
'one'
'two'
...
'nine'
"""


import soundfile as sf
import numpy as np
import os
import random
import pickle

datadir = "training_data"
CATEGORIES = os.listdir(datadir)
training_data = []

for category in CATEGORIES:
    path = os.path.join(datadir, category)
    class_number = CATEGORIES.index(category)
    for obj in os.listdir(path):
        data, _ = sf.read(os.path.join(path, obj), dtype="float32")
        data = np.delete(data, list(range(0, data.shape[0], 2)), axis=0)
        training_data.append([data, class_number])
        print(obj)

random.shuffle(training_data)
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
