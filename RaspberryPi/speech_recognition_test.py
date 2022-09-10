import sounddevice as sd
import tflite_runtime.interpreter as tflite
import numpy as np
import time


# alphabetically ordered categories
categories = ["eight", "five", "four", "nine", "no", "one", "seven", "six", "three", "two", "yes", "zero"]

interpreter = tflite.Interpreter(model_path="speech_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# parameters for sound recording
samplerate = 8000
sec = 3

# for i in range(1,4):
#     print(i)
#     time.sleep(1)
print("start")
rec = sd.rec(samplerate*sec, samplerate=samplerate, channels=1)
sd.wait()
print("end")

# find and play passage with spoken language
threshold = 0.01
for i in range(samplerate*sec):
    if abs(rec[i][0]) > threshold:
        if i > 1000:
            rec_short = rec[i-1000:i+samplerate-1000]
            print(i)
            break
sd.play(rec_short, samplerate)
sd.wait()

#preprocess for prediction
rec_short = np.expand_dims(rec_short, 0)
rec_short = rec_short*10

#predict output
interpreter.set_tensor(input_details[0]["index"], rec_short)
time.sleep(.5)
interpreter.invoke()
time.sleep(.5)

# print prediction and confidence
idx = np.argmax(interpreter.get_tensor(output_details[0]["index"]))
print(categories[idx])
print(interpreter.get_tensor(output_details[0]["index"]))
