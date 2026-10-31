class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

radius = float(input("Enter radius: "))
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

c = Circle(radius)
r = Rectangle(length, breadth)

for shape in [c, r]:
    print("Area:", shape.area())