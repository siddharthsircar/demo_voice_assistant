import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError


# constants
CHUNK = 1024 * 2  # samples per frame
FORMAT = pyaudio.paInt16  # audio format (bytes per sample)
CHANNELS = 1  # single channel for microphone
RATE = 44100  # samples per second

# create matplotlib figure and axes
fig, ax = plt.subplots(1, figsize=(15, 8))

# create pyaudio instance
p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)

# create a line object from random data
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# Basic formatting for the axes
ax.set_title('Audi Waveform')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0, 250)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK])  # , yticks=[-255, -128, 0, 128, 255])
plt.show(block=False)
print('stream started')

# for measuring frame count
frame_count = 0
start_time = time.time()

while True:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
    except TclError:
        frame_rate = frame_count / (time.time() - start_time)
        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break
