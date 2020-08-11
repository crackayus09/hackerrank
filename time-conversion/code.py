#!/bin/python3
s = input()
if s[-2:] == 'PM':
    hour = int(s[:2])
    val = str(hour + 12) if hour < 12 else s[:2]
    print(val + s[2:-2])
elif s[-2:] == 'AM' and s[:2] == '12':
    print('00' + s[2:-2])
else:
    print(s[:-2])

