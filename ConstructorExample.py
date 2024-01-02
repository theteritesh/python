class Person:
    def __init__(self,rollNo,name,age):
        self.rollNo=rollNo
        self.name=name
        self.age=age
        print("Object Is Created....")

obj=Person(100,"Ritesh",21)
print("Roll No =",obj.rollNo)
print("Name Is =",obj.name)
print("Age =",obj.age)