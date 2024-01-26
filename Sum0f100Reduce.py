from functools import reduce
l=[]
for i in range(1,101):
    l.append(i)

sum=reduce(lambda a,b:a+b,l)
print(sum)