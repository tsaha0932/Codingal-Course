from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape: Shape):
    return shape.area()

if __name__ == "__main__":
    shapes = [
        Circle(radius=5),
        Rectangle(length=4, width=6),
        Triangle(base=3, height=7)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {calculate_area(shape):.2f}")
