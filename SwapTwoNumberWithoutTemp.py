def swap(a,b):
    print("Value Before Swapping num1 =",a," num2 =",b)
    a=a+b
    b=a-b
    a=a-b
    print("Value Before Swapping num1 =",a," num2 =",b)

num1=10
num2=20
swap(num1,num2)