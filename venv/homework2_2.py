class circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius

a = int(input("tell me the r of the circle and I will tell you its area and perimeter\n>>> "))


circle_1 = circle(a)

print(circle_1.area())
print(circle_1.perimeter())
