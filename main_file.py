import matplotlib.pyplot as plt
import numpy as np

''' Script to visualize common lentghts of words in texts '''

def packing_words():
    for i in file_read:
        if len(i) in words:
            words[len(i)] += 1
        else:
            words[len(i)] = 1

with open('sample.txt', 'r') as f:
    file_read = f.read().split()

words = {}
packing_words()

# Plotting the actual data

plt.bar(words.keys(), words.values())
plt.xticks(np.arange(1, (len(words) + 1 )))
plt.xlabel('Words with this many chars'), plt.ylabel('Occurance')

plt.show()