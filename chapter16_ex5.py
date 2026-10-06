from jupyturtle import Turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f'Circle(center={self.center}, radius={self.radius})'

    def draw(self, turtle):
        turtle.move_to(self.center.x, self.center.y)
        turtle.circle(self.radius)


# Tạo Point làm tâm
center = Point(100, 100)

# Tạo Circle
circle = Circle(center, 50)

# In Circle
print(circle)

# Vẽ Circle
turtle = Turtle()
circle.draw(turtle)