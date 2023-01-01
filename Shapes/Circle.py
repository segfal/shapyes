from Shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y, 0)
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return "Circle: x = %d, y = %d, radius = %d" % (self.getx(), self.gety(), self.getRadius())
    

