import matplotlib.pyplot as graph
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

def graph(file):
fs, data = wavfile.read(file)
a = data.T[0:data.size]
b=[(ele/2**8.)*2-1 for ele in a]
c = fft(b)
d = len(c)//2
graph.plot(abs(c[:(d-1)]),'r') 
graph.show()
