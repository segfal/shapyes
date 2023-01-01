
from Circle import Circle
from Square import Square
from math import pi

class Cylinder(Circle,Square):
    def __init__(self, x, y, radius, height):
        Circle.__init__(self, x, y, radius)
        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def volume(self):
        return pi * self.getRadius() ** 2 * self.height

    def surfaceArea(self):
        return 2 * pi * self.getRadius() * self.height + 2 * pi * self.getRadius() ** 2

    def __str__(self):
        return "Cylinder: x = %d, y = %d, radius = %d, height = %d" % (self.getx(), self.gety(), self.getRadius(), self.getHeight())
    
