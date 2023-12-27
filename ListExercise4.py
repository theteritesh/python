# Concatenate two lists in the following order

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
l=[]

for i in list1:
    for j in list2:
        l.append(i+j)

print(l)