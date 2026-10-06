class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, corner, height):
        self.width = width
        self.corner = corner
        self.height = height

    def midpoint(self):
        x = (self.corner.x + self.width) / 2
        y = (self.height + self.corner.x) / 2
        return Point(x, y)

corner = Point(3, 4)
a = Rectangle(10, corner, 8)
mid = a.midpoint()

print(mid.x)
print(mid.y)

