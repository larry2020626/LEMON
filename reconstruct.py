import numpy as np
import sys

input_file = open("graph/BlogCatalog/BlogCatalog_motif.count")
counts = [0 for i in range(9)]
for line in input_file:
    nums = [int(x) for x in line.split()]
    for i in range(9):
        counts[i] += nums[i]
input_file.close()

input_file = open("graph/BlogCatalog/BlogCatalog_motif.count")
output = open("graph/BlogCatalog/reconstruct_network_new", "w")
id = 0 
for line in input_file:
    nums = [int(x) for x in line.split()]
    for i in range(9):
        motif = "motif" + str(i)
        if counts[i] != 0 and nums[i] != 0:
            weight = 1.0 * nums[i]/counts[i]
            output.write(motif + " " + str(id) + " " + str(weight) + "\n")
    id += 1
input_file.close()
output.close()
