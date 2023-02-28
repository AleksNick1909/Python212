from math import pi


class Sphere:
    x = 0
    y = 0
    z = 0

    def __init__(self, rad):
        self.rad = rad

    def get_radius(self):
        return f"get_radius: {self.rad}"

    def get_volume(self):
        return f"get_volume: {(self.rad ** 3) * pi * 4 / 3}"

    def get_square(self):
        return f"get_square: {(self.rad ** 2) * pi * 4}"

    def get_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return f"get_center: ({self.x}, {self.y}, {self.z})"

    def is_point_inside(self, x, y, z):
        return f"is_point_inside: {(self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.rad ** 2}"

    def set_radius(self, r):
        self.rad = r
        return f"set_radius({self.rad}): {self.rad}"


p1 = Sphere(0.6)
print(p1.get_radius())
print(p1.get_volume())
print(p1.get_square())
print(p1.get_center(0, 0, 0))
print(p1.get_square())
print(p1.is_point_inside(0, -1.5, 0))
print(p1.set_radius(1.6))
print(p1.is_point_inside(0, -1.5, 0))
