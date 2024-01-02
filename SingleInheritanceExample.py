class Vahicle:
    name="maruti"
    def displayVahicle(self):
        print("Name =",self.name)

class Price(Vahicle):
    price=200
    def displayPrice(self):
        print("price =",self.price)

obj=Price()
obj.displayVahicle()
obj.displayPrice()
