class Vahicle:
    def __init__(self,name):
        self.name=name
    def displayV(self):
        print("Name =",self.name)

class Category(Vahicle):
    def __init__(self,name,price):
        Vahicle.__init__(self,name)
        self.price=price
    def displayC(self):
        print("Price=",self.price)

obj=Category("Marutu",2000)
obj.displayC()
obj.displayV()
obj=Category("Aulto",3000)
obj.displayC()
obj.displayV()