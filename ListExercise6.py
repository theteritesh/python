# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
l=list(filter(None,list1))
print(l)