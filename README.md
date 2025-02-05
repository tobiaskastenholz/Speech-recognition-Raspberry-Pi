# Speech-recognition-Raspberry-Pi

This is the code for a work-in-progress speech recognition project on a Raspberry Pi 4.

The goal is to create a program that runs on a Raspberry Pi and starts a conversation as soon as an
ultrasonsic sensor registers movement in the environment. In my setup, the Raspberry Pi is connected
to a small Bluetooth speaker with a microphone that is used for input and output of sound.

**Currently supported:**

Preprocess speech recognition dataset from  
https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data  
using the SoundFile library.


Train speech recognition model using TensorFlow and save as tflite model to later run on a Raspberry Pi.
Unfortunately, the preprocessed data is too large to be uploaded on GitHub, 
so please download the dataset and run the preprocessing yourself, as described above. 

Files in 'RaspberryPi' directory are executed directly on the Pi:
- speech_recognition_test.py for testing the tflite speech model. The library sounddevice is used for input and output sound data.
- read_ultrasonic_sensor.py for reading ultrasonic sensor every second and printing measured distance.
- ping.py for running in the background to prevent Bluetooth speaker from turning off.


