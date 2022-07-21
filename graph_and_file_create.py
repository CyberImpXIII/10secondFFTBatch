from asyncore import read, write
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile  # get the api


def graph(file, filename, output, input):
    print('graphing', file)
    fs, data = wavfile.read(input + file)
    a = data.T[0:data.size]
    b = [(ele/2**8.)*2-1 for ele in a]
    c = fft(b)
    d = len(c)//2
    plt.plot(abs(c[:(d-1)]), 'r')
    plt.savefig(output + '/' + filename + '.png', bbox_inches='tight')
