r=int(input("Enter the Range ="))
first=0
second=1
while (first<=r):
    print(first,end=" ")
    fib=first+second
    first=second
    second=fib