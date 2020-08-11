#!/bin/python3
n = int(input())
s = input()

path = s[:n]

summed = 0
count = 0
for d in path:
    if d == 'U':
        summed += 1
        if summed == 0:
            count += 1
    else:
        summed -= 1
print(count)
