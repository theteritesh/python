d={
    "name":"Ritesh",
    "Salary":5000,
    "Dipart":"Manegement"
}
d["age"]=21
print(d)

print(d.get('age'))

for i in  d.keys():
    print(i,end=" ")
print()
for i in  d.values():
    print(i,end=" ")

print()

for i,j in d.items():
    print(i,"-->",j)
