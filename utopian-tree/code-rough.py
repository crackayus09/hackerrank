#!/bin/python3

t = int(input())

for t_itr in range(t):
    n = int(input())
    height = 1
    if n > 0:
        for i in range(0, n):
            if i % 2 == 0:
                height *= 2
            else:
                height += 1
        print(height)
    else:
        print(1)

