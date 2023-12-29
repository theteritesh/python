# Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


from turtle import update


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d={}
for i in keys:
    v=sample_dict.get(i)
    d.update({i:v})

print(d)