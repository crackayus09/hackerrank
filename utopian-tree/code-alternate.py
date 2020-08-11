#!/bin/python3

# This approach is for large systems who can produce the series once and cache it. This will be more processing but can be reused. Each reuse should take very less time.

t = int(input())

inputs = []
for t_itr in range(t):
    inputs.append(int(input()))
inputsSorted = sorted(inputs)

takes = [0, 1]
canBeCached = {0 : 1}
for i in inputsSorted:
    if i > 0:
        inpVal = takes[0]
        height = takes[1]
        for j in range(inpVal + 1, i + 1):
            if j % 2 == 0:
                height += 1
            else:
                height *= 2
        takes = [i, height]
        canBeCached[i] = height
for i in inputs:
    print(canBeCached[i])

