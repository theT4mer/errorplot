import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd
import sys

def is_valid_timestamp(timestamp):
    try:
        datetime.utcfromtimestamp(timestamp)
        return True
    except:
        return False

#open data file and read data + split data line by line
datastream = open("path/to/file/raw_data.txt", "r")
content_of_lines = datastream.readlines()
length = len(content_of_lines)

#declare the array for the data so that we can write into it
data = np.empty((length, 2),int)

# reformat the data to a int list
#declare the array for the timestamp in the diagram
timestamp = np.empty(length, dtype='S19')
i=0
for line in content_of_lines:
    line = line.replace("\n", "")
    split_line = [int(i) for i in line.split(";") if i.isdigit()]
    data[i][0] = split_line [0] + split_line[1] + split_line[2] + split_line[3] + split_line[4]
    data[i][1] = split_line[5]
    #convert the timestamp to a datetime object while checkingfor if the timestamp is valid
    if is_valid_timestamp(data[i][1]):
        timestamp[i] = datetime.utcfromtimestamp(data[i][1]).strftime('%Y-%m-%d %H:%M:%S')
    else:
        print("Invalid timestamp:", data[i][1])
        sys.exit("program stopped")
    i+=1

print('data:', data)

# Close the file
datastream.close()

print('timestamp:', timestamp)
#plt.subplots_adjust(top=1)  # Adjust space at the top of the plot
plt.figure(figsize=(16, 9))
plt.subplots_adjust(bottom=0.18)  # Adjust space at the bottom of the plot
plt.bar(timestamp, data[:,0], color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Fehler in Abhängigkeit der Zeit')
plt.xticks(rotation=30)  # Rotate labels on x-axisplt.savefig('Diagrams/Diagramm_Laboraufgabe_1.pdf', dpi=300)
plt.subplots_adjust(left=0.07, right=0.99, top=0.95)
plt.savefig('path/to/file/example.pdf', dpi=300)
plt.show()