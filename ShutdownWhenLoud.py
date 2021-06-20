import sounddevice as sd
import numpy as np
import os

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if volume_norm > 100:
        #adjust sound here
        os.system('shutdown /p /f')
        #change this to print something since it suddenly turns ur pc while testing

with sd.Stream(callback=print_sound):
    sd.sleep(6000000)
