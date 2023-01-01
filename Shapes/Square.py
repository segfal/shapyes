from Shape import Shape


class Square(Shape):
    def __init__(self, x, y, side):
        Shape.__init__(self, x, y, 0)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return "Square: x = %d, y = %d, side = %d" % (self.getx(), self.gety(), self.getSide())

