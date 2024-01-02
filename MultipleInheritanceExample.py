class Father:
    def displayF(self):
        print("Father")

class Mother:
    def displayM(self):
        print("Mother")

class Son(Father,Mother):
    def displayS(self):
        print("Son")

obj=Son()
obj.displayS()
obj.displayM()
obj.displayF()
    