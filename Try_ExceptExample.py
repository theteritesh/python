a=10
b=0
try:
    a/b
except ZeroDivisionError:
    print("Divide By Zero Error")
else:
    print(a/b)