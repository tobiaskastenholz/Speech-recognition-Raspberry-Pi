"""
keep this script running to keep Bluetooth speaker turned on
"""

import sounddevice as sd
import time
import numpy


rec = numpy.zeros(8000)

while True:
    sd.play(rec,8000)
    sd.wait()
    time.sleep(60)