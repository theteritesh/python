row=int(input("Enter no row:"))
for i in range(1,row):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()