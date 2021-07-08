# class Triangle:
#     num = 0
#
#     def __init__(self, h, a, b, c):
#         self.height = h
#         self.a_side = a
#         self.b_side = b
#         self.c_side = c
#
#     def __new__(cls, *args, **kwargs):
#         cls.num +=1
#         return super().__new__(cls)
#
#
#     def area(self):
#         return self.height * self.b_side / 2
#
#     def perimeter(self):
#         return self.a_side + self.b_side + self.c_side
#
#     def compare(self):
#         if triangle_1.area() < triangle_2.area():
#             print(f"{triangle_1.area()} < {triangle_2.area()} that means that the area of first instance is greater than the second instance")
#         elif triangle_1.area() > triangle_2.area():
#             print(f"{triangle_1.area()} > {triangle_2.area()} that means that the area of first instance is less than the second instance")
#         else:
#             print(f"{triangle_1.area()} = {triangle_2.area()} that means that the area of first instance is equal to the second instance")
#
#
#     def is_alike(self, other):
#         if self.a_side % other.a_side == 0 and self.b_side % other.b_side == 0 and self.c_side % other.c_side == 0:
#             print("The triangles are like each other")
#         else:
#             print("The triangles are not similar")
#
# e = int(input("Tell me the height of the triangle\n>>> "))
# t = int(input("Tell me the side of the triangle\n>>> "))
# w = int(input("Tell me the base of the triangle\n>>> "))
# q = int(input("Tell me the another side of the triangle\n>>> "))
#
# triangle_1 = Triangle(e, t, w, q)
# triangle_2 = Triangle(2, 6, 5, 6)
#
#
# if w + t < q or w + q < t or q + t < w:
#     print("There is no such triangle.")
# else:
#     print(f"The area of 1st instance is {triangle_1.area()}")
#     print(f"The perimeter 1st instance is {triangle_1.perimeter()}")
#     print(f"The area of 2nd instance is {triangle_2.area()}")
#     print(f"The perimeter 2nd instance is {triangle_2.perimeter()}")
#     print(Triangle.num)
#     print(triangle_1.compare())
#     print(triangle_1.is_alike(triangle_2))

# class Cube:
#     def __init__(self):


class Rectangle:
    def __init__(self, a, b, c, d):
        self.l_side = a
        self.u_side = b
        self.r_side = c
        self.d_side = d

    def area(self):
        return self.l_side * self.u_side

    def perimeter(self):
        return self.l_side + self.u_side + self.r_side + self.d_side



    def compare(self):
        if rectangle_1.area() < rectangle_2.area():
            print(f"{rectangle_1.area()} < {rectangle_2.area()} that means that the area of first instance is greater than the second instance")
        elif rectangle_1.area() > rectangle_2.area():
            print(f"{rectangle_1.area()} > {rectangle_2.area()} that means that the area of first instance is less than the second instance")
        else:
            print(f"{rectangle_1.area()} = {rectangle_2.area()} that means that the area of first instance is equal to the second instance")

a = int(input("Tell me the 1st side of the rectangle\n>>> "))
b = int(input("Tell me the 2nd side of the rectangle\n>>> "))
c = int(input("Tell me the 3rd side of the rectangle\n>>> "))
d = int(input("Tell me the 4th side of the rectangle\n>>> "))

rectangle_1 = Rectangle(a, b, c, d)
rectangle_2 = Rectangle(5, 6, 5, 6)

print(f"The area of 1st instance is {rectangle_1.area()}")
print(f"The perimeter 1st instance is {rectangle_1.perimeter()}")
print(f"The area of 2nd instance is {rectangle_2.area()}")
print(f"The perimeter 2nd instance is {rectangle_2.perimeter()}")
print(rectangle_1.compare())
