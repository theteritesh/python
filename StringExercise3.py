# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters

s1=input("Enter First String =")
s2=input("Enter Second String =")

s1mid=len(s1)//2
s2mid=len(s2)//2

s3=s1[0]+s2[0]+s1[s1mid]+s2[s2mid]+s1[-1]+s2[-1]

print(s3)