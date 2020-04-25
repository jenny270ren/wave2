import random
n= int(random.randint(0,38))
print ("The spin resulted in",n,"...")
if(n==0):
    print("Pay 0")
elif(n==38):
    print("Pay 00")
else:
    print ("Pay",n)
    if(n==1 or n==3 or n==5 or n==7 or n==9 or n==12 or n==14 or n==16 or n==18 or n==21 or n==23 or n==25 or n==27 or n==30 or n==32 or n==34 or n==36):
        print("Pay Red")
    else:
        print ("Pay Black")
    if(n%2==1):
        print("Pay Odd")
    else:
        print("Pay Even")
    if(n<19):
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")






