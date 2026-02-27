class Polygon:
    def __init__(self, n_side):
        self.n = n_side
        self.side = [0 for i in range(n_side)]
    
    def create_polygon(self):
        self.n = int(input('Enter number of sides: '))
        self.side = [float(input(f'Enter side {i+1}: ')) for i in range(self.n)]

        print(f'Polygon was created. They have {self.n} sides.')

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        

    def find_area(self):
        a, b, c = self.side
        p = (a + b + c) / 2
        area = (p * (p-a) * (p-b) * (p-c)) ** 0.5
        print(f"The area of triangle equal:{round(area, 2)}")
        


t = Triangle()

t.create_polygon()

t.find_area()



