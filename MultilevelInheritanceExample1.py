class Grandfather:
    def DisplayG(self):
        print("Grandfather")
class Father(Grandfather):
    def DisplayF(self):
        print("Father")
class Son(Father):
    def DisplayS(self):
        print("Son")

obj=Son()
obj.DisplayS()
obj.DisplayF()
obj.DisplayG()