from Square import Square


class Cube(Square):
    def __init__(self, x, y, side):
        Square.__init__(self, x, y, side)

    def volume(self):
        return self.getSide() * self.getSide() * self.getSide()

    def surfaceArea(self):
        return 6 * self.getSide() * self.getSide()

    def __str__(self):
        return "Cube: x = %d, y = %d, side = %d" % (self.getx(), self.gety(), self.getSide())
    

