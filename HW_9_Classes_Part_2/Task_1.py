import math


class Shape(object):
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        raise NotImplementedError('perimeter() is not implemented')

    def area(self):
        raise NotImplementedError('area() is not implemented')


class Triangle(Shape):
    def __init__(self, sides):
        if len(sides) != 3:
            raise Exception('Triangle expects exactly 3 sides')

        for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            if sides[a] >= (sides[b] + sides[c]) or sides[a] <= (abs(sides[b] - sides[c])):
                raise Exception('Invalid sides')

        super().__init__(sides)

    def perimeter(self):
        return self.sides[0] + self.sides[1] + self.sides[2]

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


class Rectangle(Shape):
    def __init__(self, sides):
        if len(sides) != 2:
            raise Exception('Rectangle expects exactly 2 sides')
        super().__init__(sides)

    def perimeter(self):
        return (self.sides[0] + self.sides[1]) * 2

    def area(self):
        return self.sides[0] * self.sides[1]


class Circle(Shape):
    def __init__(self, sides):
        if len(sides) != 1:
            raise Exception('Circle expects exactly 1 side (radius)')
        super().__init__(sides)

    def perimeter(self):
        return 2 * math.pi * self.sides[0]

    def area(self):
        return math.pi * (self.sides[0] ** 2)


t = Triangle([3, 4, 5])
print(t.perimeter())
print(t.area())

r = Rectangle([3, 5])
print(r.perimeter())
print(r.area())

ci = Circle([4])
print(ci.perimeter())
print(ci.area())
