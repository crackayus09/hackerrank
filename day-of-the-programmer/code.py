#!/bin/python3
year = int(input().strip())

if (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
    print('12.09.'+str(year))
elif year == 1918:
    print('26.09.1918')
else:
    print('13.09.'+str(year))

