import random as r
comNumber=r.randint(0,100)
a=1
while a:
    print("Enter Your Number(0 to 100) to Gess The perfect Computer Grenerted Number =")
    n=int(input()) 
    if n==comNumber:
        print("You Won ")
        print("You gess correct number as ",n)
        a=0
    elif n>comNumber:
        print("Try again The number is grater than  computer number")
        continue
    elif n<comNumber:
        print("Try again The number is lesser than  computer number")
        continue