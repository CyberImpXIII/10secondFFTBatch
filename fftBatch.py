import glob

from numpy import true_divide
from graph_and_file_create import *
import sys
import os

input = './'
output = './output'
graphprint = True
csvprint = True

for argument in sys.argv:
    if("INPUT=" in argument.upper()):
        if(argument.split('=')[1].strip('\"').strip('\'') == './' or argument.split('=')[1].strip('\"').strip('\'') == './input'):
            print('no need to include' + argument.split('=')
                  [1] + 'in your function call as it is supported by default')
        input = argument.split('=')[1].strip('\"').strip('\'')
    if("OUTPUT=" in argument.upper()):
        if(argument.split('=')[1] == './output'):
            print(
                'no need to include ./output in your function call as it is supported by default')
        output = argument.split('=')[1].strip('\"').strip('\'')
    if('GRAPH=' in argument.upper()):
        graphprint = argument.split('=')[1].lower().strip(
            '\"').strip('\'') == 'true'
    if('CSV=' in argument.upper()):
        csvprint = argument.split('=')[1].lower().strip(
            '\"').strip('\'') == 'true'

if glob.glob(output):
    if(graphprint == True & csvprint == True):
        print('placing graph files and fft csv files in', output)
    elif(graphprint == True):
        print('placing graph files in', output)
    elif(csvprint == True):
        print('placing fft csv files in', output)
else:
    print('output folder does not exist or is not valid, using default output folder')
    if(graphprint == True & csvprint == True):
        print('placing graph files and fft csv files in', output)
    elif(graphprint == True):
        print('placing graph files in', output)
    elif(csvprint == True):
        print('placing csv files in', output)

    if(len(glob.glob('./output')) == 0):
        print('creating output')
        os.mkdir('./output')
    output = './output'

if(graphprint and not glob.glob(output + '/graph')):
    os.mkdir(output + '/graph')

if(csvprint and not glob.glob(output + '/csv')):
    os.mkdir(output + '/csv')

if glob.glob(input):
    print('placing graph files and fft csv files in', input)
else:
    print('input folder does not exist or is not valid')
    if(glob.glob('./input')):
        print('folder named input detected, importing files from input')
        input = './input'
    else:
        print('importing files from current directory')
        input = './'

files = glob.glob(input + '*.wav')
for file in files:
    graph(file, file.replace('./', '').replace('.wav', ''),
          output, input, graphprint, csvprint)
quit()
