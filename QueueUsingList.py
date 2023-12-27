l=[]

while 1:
    c=int(input("""
        1 Enqueue ELEMENT
        2 Dequeue ELEMENT
        3 FIRST ELEMENT
        4 REAR ELEMENT
        5 DISPLAY Queue
        6 EXIT
    """))
    if c==1:
        n=int(input("Enter Element to push ="))
        l.append(n)
    elif c==2:
        if len(l)==0:
            print("Queue is empty..")
        else:
            p=l.pop(0)
            print("Poped Element =",p)
    elif c==3:
        if len(l)==0:
            print("Queue is empty..")
        else:
            p=l[0]
            print("First Element =",p)
    elif c==4:
        if len(l)==0:
            print("Queue is empty..")
        else:
            p=l[-1]
            print("Last Element =",p)
    elif c==5:
        if len(l)==0:
            print("Queue is empty..")
        else:
            print(l)

    elif c==6:
        break

    else:
        print("Invalid Input")