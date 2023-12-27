l=[10,20,30,40,50,60,20,40,20,30,20]

#count

c=l.count(20) #return count of given value from list 
print("Count of 10 -",c)

#max()

print("Maximum Value of List -",max(l))  #return maximum value fro list

#MIN
print("Minumum Value of List -",min(l))  #return minimum value fro list

#sort
print("list Before Sorting- ",l)
l.sort()   #sort list in ascending order
print("list After Sorting- ",l)

#reverse
print("list Before Reverse- ",l)
l.reverse()  #reverse all values of list
print("list After Reverse- ",l)

#index
i=l.index(30) #return index number of given value
print("Index Number OF 30 -",i)