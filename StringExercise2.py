# Given two strings, s1 and s2. Write a program to create a new string s3 by 
# appending s2 in the middle of s1.

s1=input("Enter First String =")
s2=input("Enter Second String =")
s1mid=len(s1)//2
s3=s1[0:s1mid]+s2+s1[s1mid:]
print(s3)