#n odd weird
#n>2 and n<5 not weird
#n even n>6 and n<20 weird
#n even n>20 not weird

#!/usr/bin/python
if __name__ =='__main__':
    n = int(raw_input('please enter the number :'))
    m = n%2
    if m == 0:
        if n >= 2 and n <= 5 :
            print ("Not Weird")
        elif n >= 6 and n <= 20 :
            print ("Weird")
        elif n > 20 :
            print ("Not Weird")
    else :
        print ("Weird")
