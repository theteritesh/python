l=[1,2,3,4,5,6,7,8,9,10,11,12]

def is_even(n):
    return n%2==0

even=list(filter(is_even,l))
print(even)