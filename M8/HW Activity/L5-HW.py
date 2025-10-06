import math
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print("Choose a shape to calculate area:")
print("1. Triangle")
print("2. Rectangle")
print("3. Square")
print("4. Circle")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    t = Triangle(base, height)
    print("Area of Triangle:", t.area())

elif choice == '2':
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    r = Rectangle(length, width)
    print("Area of Rectangle:", r.area())

elif choice == '3':
    side = float(input("Enter side of square: "))
    s = Square(side)
    print("Area of Square:", s.area())

elif choice == '4':
    radius = float(input("Enter radius of circle: "))
    c = Circle(radius)
    print("Area of Circle:", c.area())

else:
    print("Invalid choice. Please select from 1 to 4.")
