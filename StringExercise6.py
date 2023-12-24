# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"
ls1=len(s1)
ls2=len(s2)
length=0
if ls1>ls2:
    length=ls1
else:
    length=ls2
s2=s2[::-1]
s3=""
for i in range(length):
    if i<ls1:
        s3=s3+s1[i]
    if i<ls2:
        s3=s3+s2[i]
print(s3)
