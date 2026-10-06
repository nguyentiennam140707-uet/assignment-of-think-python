class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return Point(x, y)


class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def make_lines(self):
        x = self.corner.x
        y = self.corner.y
        w = self.width
        h = self.height

        p1 = Point(x, y)
        p2 = Point(x + w, y)
        p3 = Point(x + w, y + h)
        p4 = Point(x, y + h)

        lines = [
            Line(p1, p2),
            Line(p2, p3),
            Line(p3, p4),
            Line(p4, p1)
        ]

        return lines

    def make_cross(self):
        lines = self.make_lines()

        midpoints = []
        for line in lines:
            midpoints.append(line.midpoint())

        cross = [
            Line(midpoints[0], midpoints[2]),
            Line(midpoints[1], midpoints[3])
        ]

        return cross