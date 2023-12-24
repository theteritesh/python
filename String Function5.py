#format

s= "Welcome {} {} your roll Number is {}".format("Ritesh","Thete",20)
print(s)

s= "Welcome {1} {0} your roll Number is {2}".format("Ritesh","Thete",20)
print(s)

s= "Welcome {b} {a} your roll Number is {c}".format(a="Ritesh",b="Thete",c=20)
print(s)

s= "Welcome {1:20} {0} your roll Number is {2}".format("Ritesh","Thete",20)
print(s)
s= "Welcome {1:<20} {0} your roll Number is {2}".format("Ritesh","Thete",20)
print(s)
s= "Welcome {1:^20} {0} your roll Number is {2}".format("Ritesh","Thete",20)
print(s)
s= "Welcome {1:>20} {0} your roll Number is {2}".format("Ritesh","Thete",20)
print(s)
