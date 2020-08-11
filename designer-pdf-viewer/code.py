#!/bin/python3

h = list(map(int, input().rstrip().split()))

word = input()

wordSet = set(word)
height = 0
count = 0
for i in wordSet:
    count += 1
    height1 = h[ord(i) - 97]
    height = height1 if height1 > height else height

print(height * len(word))

