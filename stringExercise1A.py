# Write a program to create a new string made of an input string’s 
# first, middle, and last character.

s=input("Enter String : ")
first=s[0]
middle=s[len(s)//2]
last=s[-1]
print(first+middle+last)