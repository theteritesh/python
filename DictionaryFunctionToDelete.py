d={
    "name":"Ritesh",
    "Salary":5000,
    "Dipart":"Manegement",
    'age':21
}
print("Before Deletetion",d)
del d["age" ]
print("After Deletetion",d)

print("Before Deletetion",d)
p=d.pop('Salary')
print("Popped Element",p)
print("After Deletetion",d)