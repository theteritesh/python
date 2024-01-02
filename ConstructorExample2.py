#Find Are of rectangle

from cmath import rect


class Rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w

obj=Rect(20,10)
print("Area Of Circle Is =",obj.area())