# Write a program to create a new string made of the middle three 
# characters of an input string.

s=input("Enter String =")
mid=len(s)//2
print(s[mid-1:mid+2])