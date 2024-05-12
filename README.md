# errorplot
Little python programm that takes raw data from a text file in a specific format and plots is in a graph. It is meant for mapping a fixed set of datapoints and plotting them in respective to a time.

My code is a bit stupid and only for a niche use-case, but i wanted to share it anyway :)

The repo is obviously still work in progress. To do's include improved error handlind, cleaning up the code and limiting the size of the diagram to a fixed size. 

The format is specified like follows: first we have five datapoints (e.g. if tests have failed). then comes a UNIX-timestamp
The datapoints are added to each other, the timestamp is converted into a human-readable format and plotted. An example of such a graph is included.











