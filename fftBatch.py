import glob
import graph_and_file_create.pt
files = glob.glob('./*.wav')
for file in files:
    graph(file)
quit()