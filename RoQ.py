import math
a = int(input())
b = int(input())
c = int(input())
r = (b**2)-(4*a*c)
if r<0:
    print ("no real roots")
elif r==0:
    r = -1*b/(2*a)
    print ("one root:",r)
else:
    r = r**0.5
    r1 = ((-1*b)+r)/(2*a)
    r2 = ((-1*b)-r)/(2*a)
    print ("two roots:", r1, r2)