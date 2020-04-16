c = input()
r = int(input())
if r%2==0:
    if c=="b" or c=="d" or c=="f" or c=="h":
        print("black")
    else:
        print("white")  
elif c=="b" or c=="d" or c=="f" or c=="h":
    print("white") 
else:
     print("black")
