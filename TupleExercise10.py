# Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45,45)
count=0
for i in tuple1:
    if tuple1[0]==i:
        count +=1

if count==len(tuple1):
    print("All are same")   
else:
    print("All are not same")   