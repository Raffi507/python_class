#1
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius

x = int(input("tell me the r of the circle and I will tell you its area and perimeter\n>>> "))


circle_1 = Circle(x)

print(circle_1.area())
print(circle_1.perimeter())


#2
class Triangle:
    def __init__(self, h, a, b, c):
        self.height = h
        self.a_side = a
        self.b_side = b
        self.c_side = c

    def area(self):
        return self.height * self.b_side / 2

    def perimeter(self):
        return self.a_side + self.b_side + self.c_side

e = int(input("Tell me the height of the triangle\n>>> "))
t = int(input("Tell me the side of the triangle\n>>> "))
w = int(input("Tell me the base of the triangle\n>>> "))
q = int(input("Tell me the another side of the triangle\n>>> "))

triangle_1 = Triangle(e, t, w, q)


if w + t < q or w + q < t or q + t < w:
    print("There is no such triangle.")
else:
    print(f"The area is {triangle_1.area()}")
    print(f"The perimeter is {triangle_1.perimeter()}")