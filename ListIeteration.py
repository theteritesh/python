l=[10,20,30,40,50,60,70]

for i in range(len(l)):
    print(l[i],end=" ")
print()

for i in l:
    print(i,end=" ")
print()
for i in range(len(l)-1,-1,-1):
    print(l[i], end=" ")