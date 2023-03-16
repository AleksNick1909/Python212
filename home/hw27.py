
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __getitem__(self, item):
        if item == "x":
            return f"x = {self.x}"
        elif item == "y":
            return f"y = {self.y}"
        elif item == "z":
            return f"z = {self.z}"

    def __setitem__(self, key, value):
        x = self.x
        y = self.y
        z = self.z

        if key == "x":
            self.x = value
        if key == "y":
            self.y = value
        if key == "z":
            self.z = value


one = Point3D(12, 15, 18)
two = Point3D(6, 3, 9)
print("Координаты 1-й точки:", one.info())
print("Координаты 2-й точки:", two.info())
res1 = one + two
print("Сложение координат:", res1.info())
res2 = one - two
print("Вычитание координат:", res2.info())
res3 = one * two
print("Умножение:", res3.info())
res4 = one / two
print("Деление:", res4.info())
if one == two:
    print("Равенство координат:", True)
else:
    print("Равенство координат:", False)
print(one["x"], two["x"])
print(one["y"], two["y"])
print(one["z"], two["z"])

one["x"] = 20
one["y"] = 5
two["z"] = 6
print("Запись значения в координату:", one["x"], one["y"], two["z"])
print(one["x"], two["x"])
print(one["y"], two["y"])
print(one["z"], two["z"])
