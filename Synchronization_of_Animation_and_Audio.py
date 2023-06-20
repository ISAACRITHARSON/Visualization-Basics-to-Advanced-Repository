import pyaudio
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('bmh')
samplesize = 4096
samplerate = 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=samplerate,
input=True, frames_per_buffer=samplesize)
fig = plt.figure()
ax = plt.axes(xlim=(0, samplesize - 1), ylim=(-9999, 9999))
line, = ax.plot([], [], lw=1)

x = np.linspace(0, samplesize - 1, samplesize)

def init():
line.set_data([], [])
return line,

def animate(i):
y = np.frombuffer(stream.read(samplesize), dtype=np.int16)
line.set_data(x, y)
return line,
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20,
blit=True)
print(anim)
plt.show()
