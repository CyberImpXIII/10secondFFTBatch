import glob
import graph_and_file_create
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

files = glob.glob('./*.wav')
for file in files:
    graph(file)
quit()
