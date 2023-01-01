from Circle import Circle
from math import pi


class Sphere(Circle):
    def __init__(self, x, y, radius):
        Circle.__init__(self, x, y, radius)

    def volume(self):
        return 4.0 / 3.0 * pi * self.getRadius() ** 3

    def surfaceArea(self):
        return 4 * pi * self.getRadius() ** 2

    def __str__(self):
        return "Sphere: x = %d, y = %d, radius = %d" % (self.getx(), self.gety(), self.getRadius())
    

