
class Integer:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение должно быть положительным")
        elif not isinstance(value, int):
            raise TypeError(f"Координаты {value} должны быть целыми числами")
        instance.__dict__[self.name] = value


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        return f"Треугольник со сторонами: ({self.a}, {self.b}, {self.c})"

    def tr(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "существует"
        else:
            return "не существует"


tr1 = Triangle(2, 5, 6)
tr2 = Triangle(5, 2, 8)
tr3 = Triangle(7, 3, 6)

print(tr1.info(), tr1.tr())
print(tr2.info(), tr2.tr())
print(tr3.info(), tr3.tr())
