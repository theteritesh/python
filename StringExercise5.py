# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"
letter=0
digit=0
symb=0
for i in str1:
    if (i.isalpha()):
        letter +=1
    elif (i.isdigit()):
        digit +=1
    else:
        symb +=1

print("Total Letters = ",letter)
print("Total Digit = ",digit)
print("Total Symbol = ",symb)