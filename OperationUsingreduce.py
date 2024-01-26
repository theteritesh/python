from functools import reduce

l=[]
for i in range(1,101):
    l.append(i)

sum=reduce(lambda a,b:a+b,l)
print("Sum =",sum)

mul=reduce(lambda a,b:a*b,l)
print("Muliplicaion =",mul)

sub=reduce(lambda a,b:a-b,l)
print("Subtraction =",sub)

div=reduce(lambda a,b:a/b,l)
print("Division =",div)