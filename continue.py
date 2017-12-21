#!/bin/python

result = []
for x in range (1, 10):
    if x % 3 != 0:
        continue
    result.append(x)
    print result
print result
