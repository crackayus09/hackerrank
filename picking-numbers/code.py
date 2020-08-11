#!/bin/python3

n = int(input().strip())
a = list(map(int, input().rstrip().split()))

aUniq = sorted(list(set(a)))

reps = []

for i in aUniq:
    reps.append(a.count(i) + a.count(i+1))

print(max(reps))
