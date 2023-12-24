# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first



str1 = "PyNaTive"
first=""
last=""
for i in str1:
    if (i.islower()):
        first=first+i
    else:
        last=last+i

str2=first+last
print(str2)