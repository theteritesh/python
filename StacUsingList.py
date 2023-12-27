
l=[]

while 1:
    c=int(input("""
        1 PUSH ELEMENT
        2 POP ELEMENT
        3 PEEK ELEMENT
        4 DISPLAY STACK
        5 EXIT
    """))
    if c==1:
        n=int(input("Enter Element to push ="))
        l.append(n)
    elif c==2:
        if len(l)==0:
            print("Stack is empty..")
        else:
            p=l.pop()
            print("Poped Element =",p)
    elif c==3:
        if len(l)==0:
            print("Stack is empty..")
        else:
            p=l[-1]
            print("Peeked Element =",p)
    elif c==4:
        if len(l)==0:
            print("Stack is empty..")
        else:
            print(l)

    elif c==5:
        break

    else:
        print("Invalid Input")