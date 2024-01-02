# Write a peogram to calculate area and C of circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def Constructor(self):
        return self.radius*2*3.14
obj=Circle(10)
print("Area =",obj.area())
print("Constructor=",obj.Constructor())