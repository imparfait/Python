import math
from abc import ABC, abstractmethod

# class Figure:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement the area method")
#     def __int__(self):
#         return int(self.area())
#     def __str__(self):
#         return f"Figure with area: {self.area()}"
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def __str__(self):
#         return f"Rectangle with width: {self.width}, height: {self.height}, area: {self.area()}"
# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def __str__(self):
#         return f"Circle with radius: {self.radius}, area: {self.area():.2f}"
# class Triangle(Figure):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
#     def __str__(self):
#         return f"Triangle with base: {self.base}, height: {self.height}, area: {self.area()}"
# class Trapezoid(Figure):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#     def area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
#     def __str__(self):
#         return f"Trapezoid with bases: {self.base1}, {self.base2}, height: {self.height}, area: {self.area()}"

# figures = [
#     Rectangle(6, 10),
#     Triangle(10, 15),
#     Trapezoid(10, 10, 7)
# ]
# for figure in figures:
#     print(figure)

class Shape(ABC):
    def show(self):
        print(self)
    @abstractmethod
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    def __str__(self):
        return f"Square with top-left corner: ({self.x}, {self.y}), side: {self.side}"
    def draw(self):
        for i in range(self.y):
            print()
        for i in range(self.side):
            print(' ' * self.x + '*' * self.side)
    
class RectangleShape(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle with top-left corner: ({self.x}, {self.y}), width: {self.width}, height: {self.height}"
    def draw(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '*' * self.width)

class CircleShape(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def __str__(self):
        return f"Circle with center: ({self.x}, {self.y}), radius: {self.radius}"
    def draw(self):
        for i in range(self.y):
            print()
        for i in range(2 * self.radius):
            for j in range(2 * self.radius):
                if (i - self.radius)**2 + (j - self.radius)**2 <= self.radius**2:
                    print(' ' * self.x + '*', end='')
                else:
                    print(' ' * self.x + ' ', end='')
            print()
 
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Ellipse with bounding box top-left: ({self.x}, {self.y}), width: {self.width}, height: {self.height}"
    def draw(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width):
                if ((i - self.height // 2)**2 / (self.height // 2)**2 + (j - self.width // 2)**2 / (self.width // 2)**2 <= 1):
                    print(' ' * self.x + '*', end='')
                else:
                    print(' ' * self.x + ' ', end='')
            print()
        
shapes = [
    Square(0, 0, 10),
    RectangleShape(5, 5, 20, 15),
    CircleShape(10, 10, 7),
    Ellipse(3, 3, 14, 10)
]
def save_shapes(filename, shapes):
    with open(filename, 'w') as f:
        for shape in shapes:
            shape_type = type(shape).__name__  
            attrs = " ".join(f"{k}:{v}" for k, v in shape.__dict__.items())  
            f.write(f"{shape_type} {attrs}\n")

def load_shapes(filename):
    loaded_shapes = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            shape_type = parts[0]  
            attributes = {kv.split(":")[0]: float(kv.split(":")[1]) for kv in parts[1:]}  
            if shape_type == "Square":
                loaded_shapes.append(Square(**attributes))
            elif shape_type == "RectangleShape":
                loaded_shapes.append(RectangleShape(**attributes))
            elif shape_type == "CircleShape":
                loaded_shapes.append(CircleShape(**attributes))
            elif shape_type == "Ellipse":
                loaded_shapes.append(Ellipse(**attributes))
    return loaded_shapes
filename = "shapes.txt"
save_shapes(filename, shapes)
loaded_shapes = load_shapes(filename)
for shape in loaded_shapes:
    shape.show()