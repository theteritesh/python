#getter And Setter

class Student:
    def __init__(self):
        self.__name=""
        self.__rollno=0
        self.__dipart=""
    def get(self):
        return self.__name,self.__rollno,self.__dipart
    def set(self,name,rollno,dipart):
        self.__name=name
        self.__rollno=rollno
        self.__dipart=dipart

obj=Student()
obj.set("Ritesh",100,"MCA")
print(obj.get())