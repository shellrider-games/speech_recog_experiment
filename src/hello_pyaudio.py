import math
from tkinter import TclError
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024*2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SECONDS = 60

def analyseAudio(data):
    pass

fig, (ax1, ax2) = plt.subplots(1, 2)

x = np.arange(0, 2*CHUNK, 2)
line, = ax1.plot(x, np.random.rand(CHUNK), '-', lw=2)
ax1.set_title('AUDIO WAVEFORM')
ax1.set_xlabel('samples')
ax1.set_ylabel('volume')
ax1.set_ylim(-2**15, 2**15)
ax1.set_xlim(0, 2*CHUNK)

ax2.set_title('FFT')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylim(0, 2**16)
ax2.set_xlim(0,CHUNK)
line2, = ax2.plot(x, np.random.rand(CHUNK), '-', lw=2)

plt.setp(ax1, xticks=[0, CHUNK, 2 * CHUNK])
plt.show(block=False)

p = pyaudio.PyAudio()
output = p.open(RATE, CHANNELS, FORMAT, output=True, frames_per_buffer=CHUNK)
input = p.open(RATE, CHANNELS, FORMAT, input=True, frames_per_buffer=CHUNK)


while(True):
    data = input.read(CHUNK)
    numericData = np.frombuffer(data, dtype=np.int16)

    analyseAudio(numericData)

    line.set_ydata(numericData)
    line2.set_ydata(np.abs(np.fft.fft(numericData)))
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
    except TclError:
        break

    # commented out for development I want to get reading done
    # output.write(data)

input.stop_stream()
input.close()
p.terminate()
