# Geometric shape class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

rectangle = Rectangle(5, 10)
print(f"Area: {rectangle.calculate_area()}, Perimeter: {rectangle.calculate_perimeter()}")
