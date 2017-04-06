#Read two integers from STDIN and print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.


#!/usr/bin/python
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    c = a + b
    d = a - b
    e = a * b
    print (c)
    print (d)
    print (e)
