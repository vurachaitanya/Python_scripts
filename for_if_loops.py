#!/bin/python
result = []
for x in range(1,10):
    if x % 2 == 0:
        print (  "is even")
    elif x % 2 == 1:
        print ( " is odd")

    else:
        break
    result.append(x)
print(result)
