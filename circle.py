class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 22/7 * self.radius * self.radius

    def perimeter(self):
        return 2 * 22/7 * self.radius

r = float(input("Enter radius of the circle: "))

c = Circle(r)

print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())