###################################################################################
# hw10.01

class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)   # rectangle has 4 sides
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#example

rect = Rectangle(7, 3)
print("Rectangle area:", rect.area())

######################################################################################