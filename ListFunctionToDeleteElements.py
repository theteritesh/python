l=[10,20,30,40,50,60,70,80,90]
print("Orignal list ",l)

#del()

del l[1] #delete element of given index no does not return value
print("After deleting an element list ",l)

#pop()

p=l.pop(0)  #delete an element of given index And return that element as value
print("After deleting an element list ",l)
print("Deleted Elmenet = ",p)

#remove()

l.remove(30) #delete the an elemnt dairect by its value without knowing he index number
print("After deleting an element list ",l)

#clear()

l.clear()       #use delete Whole List
print("After deleting Whole list ",l)