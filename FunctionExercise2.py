# Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable length of arguments and print their value.

# Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

def display(*args):
    for i in args:
        print(i)
    

display(10,20,30,40)

display(50,60)