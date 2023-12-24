s="My name is RITESH"
l=len(s)
print(l)
for i in range(l):
    print(s[i],end=" ")

#reverse
# Method 1
print()
for i in range(l-1,-1,-1):
    print(s[i],end=" ")

# Method 2
print()
s=s[-1::-1]  #first reverse String

for i in range(l):
    print(s[i],end=" ")