import re
import numpy as np
import scipy as sp
from scipy.spatial import distance as sp_distance
import math


words_indices = {}
words_freq = []

with open('sentences.txt', 'r') as f:
    for line in f:
        line = line.strip().lower()
        words = [x for x in re.split('[^a-z]', line) if x]
        freq = {}
        for w in words:
            if w not in words_indices:
                words_indices[w] = len(words_indices)
            if w not in freq:
                freq[w] = 0
            freq[w] += 1
        words_freq.append(freq)

matrix = []
for freq in words_freq:
    row = [0] * len(words_indices)
    for w, f in freq.items():
        row[words_indices[w]] = f
    matrix.append(row)

matrix = np.array(matrix)
second_nearest = [math.inf, 0]
nearest = [math.inf, 0]
#distances = []
for row in range(1, len(matrix)):
    distance = sp_distance.cosine(matrix[0], matrix[row])
    #distances.append(distance)
    if nearest[0] > distance:
        second_nearest = nearest[:]
        nearest[0] = distance
        nearest[1] = row

#print(nearest, second_nearest)
#print(distances)

with open('submission-1.txt', 'w') as f:
    f.write("{} {}".format(nearest[1], second_nearest[1]))