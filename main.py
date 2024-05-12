import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import sys

def is_valid_timestamp(timestamp):
    try:
        datetime.utcfromtimestamp(timestamp)
        return True
    except:
        return False

#open data file and read data + split data line by line
datastream = open("/path-to-file/raw_data.txt", "r")
content_of_lines = datastream.readlines()
length = len(content_of_lines)

data = []

# reformat the data to a int list
for line in content_of_lines:
    line = line.replace("\n", "")
    split_line = [int(i) for i in line.split(";") if i.isdigit()]
    data.append(split_line)

print('data:', data)

# Close the file
datastream.close()

#declare the for the timestamp in the diagram
timestamp = []

# Add the data so that we can see when the errors happend and remove the rest of the data
for sublist in data:
    sublist[0] = sublist[0] + sublist[1] + sublist[2] + sublist[3] + sublist[4]
    sublist[1] = sublist[5]
    del sublist[2:]
    #convert the timestamp to a datetime object while checkingfor if the timestamp is valid
    if is_valid_timestamp(sublist[1]):
        timestamp.append(datetime.utcfromtimestamp(sublist[1]).strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print("Invalid timestamp:", sublist[1])
        sys.exit("program stopped")


# Print the data for debugging
for sublist in data:
    for number in sublist:
        print(number)


values = []
for sublist in data:
    #timestamp.append(sublist[1])
    values.append(sublist[0])

#plt.subplots_adjust(top=1)  # Adjust space at the top of the plot
plt.subplots_adjust(bottom=0.18)  # Adjust space at the bottom of the plot
plt.bar(timestamp, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Fehler in Abhängigkeit der Zeit')
plt.xticks(rotation=30)  # Rotate labels on x-axis
plt.show()