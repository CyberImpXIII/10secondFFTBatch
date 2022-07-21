import glob
from graph_and_file_create import *
import sys
import os

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

files = glob.glob('./*.wav')
if glob.glob(sys.argv[1]):
    print('placing graph files and fft csv files in', sys.argv[1])
    output = sys.argv[1]
else:
    print('output folder does not exist or is not valid, using default output folder')
    print('placing graph files and fft csv files in output')
    if(glob.glob('./output')[0] != './output'):
        print('creating output')
        os.mkdir('./output')
    output = './output'
if glob.glob(sys.argv[2]):
    print('placing graph files and fft csv files in', sys.argv[2])
    input = sys.argv[2]
else:
    print('input folder does not exist or is not valid')
    if(glob.glob('./input')):
        print('folder named input detected, importing files from input')
        input = './input'
    else:
        print('importing files from current directory')
        input = './'
for file in files:
    graph(file, output, input)
quit()
