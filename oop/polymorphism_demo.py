import math
class Shape:
    
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self,length:float,width:float):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
        
    def __str__(self):
        return f"The area of the rectangle is: {self.length * self.width} "

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2
    
    def __str__(self):
        return f"The area of the Circle is: {math.pi * self.radius **2}"
    
    
    
     