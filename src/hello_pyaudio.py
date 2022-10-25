import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SECONDS = 10

def analyseAudio(data):
    print(data)

p = pyaudio.PyAudio()
output = p.open(RATE,CHANNELS,FORMAT,output=True,frames_per_buffer=CHUNK)
input = p.open(RATE,CHANNELS,FORMAT,input=True,frames_per_buffer=CHUNK)

for i in range(int(RATE / CHUNK * SECONDS)):
    data = input.read(CHUNK)
    numericData = np.frombuffer(data,dtype=np.int16)
    analyseAudio(numericData)
    #output.write(data)

input.stop_stream()
input.close()
p.terminate()