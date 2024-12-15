import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Shape:
    def show(self):
        print(self)
    def draw(self, ax):
        raise NotImplementedError("Draw method must be implemented in subclasses")

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
    def __str__(self):
        return f"Square with top-left corner: ({self.x}, {self.y}), side: {self.side}"
    def draw(self, ax):
        rect = patches.Rectangle((self.x, self.y), self.side, self.side, edgecolor='blue', facecolor='none', lw=2)
        ax.add_patch(rect)
class RectangleShape(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle with top-left corner: ({self.x}, {self.y}), width: {self.width}, height: {self.height}"
    def draw(self, ax):
        rect = patches.Rectangle((self.x, self.y), self.width, self.height, edgecolor='green', facecolor='none', lw=2)
        ax.add_patch(rect)
class CircleShape(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def __str__(self):
        return f"Circle with center: ({self.x}, {self.y}), radius: {self.radius}"
    def draw(self, ax):
        circle = patches.Circle((self.x, self.y), self.radius, edgecolor='red', facecolor='none', lw=2)
        ax.add_patch(circle)

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Ellipse with bounding box top-left: ({self.x}, {self.y}), width: {self.width}, height: {self.height}"
    def draw(self, ax):
        ellipse = patches.Ellipse((self.x + self.width / 2, self.y + self.height / 2), self.width, self.height, 
                                  edgecolor='purple', facecolor='none', lw=2)
        ax.add_patch(ellipse)
shapes = [
    Square(1, 1, 4),
    RectangleShape(6, 6, 8, 4),
    CircleShape(15, 5, 3),
    Ellipse(20, 10, 6, 4)
]

fig, ax = plt.subplots()
ax.set_xlim(0, 30)
ax.set_ylim(0, 20)
ax.set_aspect('equal', adjustable='box')

for shape in shapes:
    shape.draw(ax)

plt.gca().invert_yaxis()  
plt.show()