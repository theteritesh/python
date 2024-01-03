#program to check ZeroDivisionError Exception
x=int(input("Enter First Value ="))
y=int(input("Enter Second Value ="))

try:
    result=x/y
except ZeroDivisionError:
    print("Division By Zero")
else:
    print("Result = ",result)
finally:
    print("Always Execute")