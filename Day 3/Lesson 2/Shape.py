class Shape(object):

    def __init__(self, fill, border):
        self.fill = fill
        self.border = border

    def printInfo(self):
        print('Fill: ', self.fill, ' Border: ', self.border)

class Circle(Shape):
    def __init__(self, fill, border, radius):
        self.fill = fill
        self.border = border
        self.radius = radius

    def perimeter(self):
            p = 2 * 3.14 * self.radius
            print(p)

    def area(self):
            a = 3.14 * self.radius * self.radius
            print(a)
testCircle = Circle('pink', 'black', 3)
testCircle.printInfo()

(testCircle.area())
(testCircle.perimeter())



class Rectangle(Shape):
    def __init__(self, fill, border, base, height):

        self.fill = fill
        self.border = border
        self.base = base
        self.height = height

    def perimeter(self):
            p = self.base * self.height
            print(p)

    def area (self):
            a = self.base + self.base + self.height + self.height
            print(a)

testRectangle = Rectangle('pink', 'black', 3, 4)
testRectangle.printInfo()

(testRectangle.area())
(testRectangle.perimeter())

class Triangle(Shape):
    def __init__(self, fill, border, height, base , side1, side2, side3):

        self.fill = fill
        self.border = border
        self.height = height
        self.base = base
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
            a = self.side1 + self.side2 + self.side3
            print(p)

    def area (self):
            p = (self.height * self.base) / 2
            print(a)

testTriangle = Triangle('pink', 'black', 3, 7, 9, 2, 5)
testTriangle.printInfo()

(testTriangle.area())
(testTriangle.perimeter())