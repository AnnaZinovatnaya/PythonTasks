class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def area(self, other):
        pass


p = Point(4, 5)
print(p.distance(Point(6, 8)))
