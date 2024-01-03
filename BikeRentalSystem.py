class Bike:
    def __init__(self,stock):
        self.stock=stock
    def display(self):
        print("Total Avilable Bikes = ",self.stock)
    def bikeRent(self,q):
        if q<=0:
            print("Invalid Inpute(Enter The positive value)")
        elif q>self.stock:
            print("Invalid Inpute(Entered value id grater than available stock)")
        else:
            self.stock=self.stock-q
            print("Rent For ",q,"Bikes = ",q*100)
            print("Available Stock =",self.stock)

obj=Bike(500)
while True:
    uc=int(input(
"""
1.Check Avilable Stock
2.Rent a Bike/Bikes(Rent per bike 100)
3.EXIT
"""
))
    if uc==1:
        obj.display()
    elif uc==2:
        n=int(input("Enter Quenty of You want To Rent ="))
        obj.bikeRent(n)
    elif uc==3:
        break
    else:
        print("Invalid Inpute...")