from asyncore import read, write
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
from scipy.io import wavfile  # get the api


def graph(file, filename, output, input):
    print('graphing', file)
    rate, data = wavfile.read(input + file)
    DURATION = data.shape[0] // rate
    N = rate * DURATION
    yf = rfft(data)
    xf = rfftfreq(N, 1 / rate)

    plt.plot(xf, np.abs(yf))
    plt.savefig(output + '/' + filename + '.png', bbox_inches='tight')
    plt.show()
