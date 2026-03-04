class Polygon:
    def find_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def find_area(self):
        return self.length * self.width


side1 = int(input("a: "))
side2 = int(input("b: "))

rectangle = Rectangle(side1, side2)
print("Area: ", rectangle.find_area())