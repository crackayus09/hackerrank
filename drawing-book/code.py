#!/bin/python3

import math

n = int(input())

p = int(input())

if math.ceil(n / 2) > p:
    print(int(p/2))
else:
    num = (n-p)/2
    if n % 2 == 0 and n / p != 2:
        print(math.ceil(num))
    else:
        print(int(num))
