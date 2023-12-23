print('''
    + Addition
    - Subraction
    * Multiplication
    / Division  
''')

opr=input("Enter the Opreation")
num1=int(input("Enetr the First Number"))
num2=int(input("Enetr the Second Number"))

if(opr=="+"):
    print("Addition")
    print(num1,"+",num2,"=",num1+num2)
elif(opr=="-"):
    print("Subtraction")
    print(num1,"-",num2,"=",num1-num2)
elif(opr=="*"):
    print("Multyplication")
    print(num1,"*",num2,"=",num1*num2)
elif(opr=="/"):
    print("Division")
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Enter Valid Operation")
