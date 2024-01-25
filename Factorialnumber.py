num=int(input("Enter the Number ="))
fact=1
if num<0:
    print("Invalid Input Does Not Enter negative value")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i

    print(f"Factorial of {num} is {fact}")