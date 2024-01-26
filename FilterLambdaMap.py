l=[1,2,3,4,5,6,7,8,9,10,11,12]

even=list(filter(lambda n:n%2==0,l))

duble=list(map(lambda n:n*2,even))

print(even)
print(duble)