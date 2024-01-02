


class Car:
    def get(self,color,style):
        self.color=color
        self.style=style
    def put(self):
        print(self.color)
        print(self.style)
obj=Car()
obj.get("sadan","Black")
obj.put()