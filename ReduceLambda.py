from functools import reduce

l=[1,2,3,4]

sum=reduce(lambda a,b:a+b,l)
print(sum)