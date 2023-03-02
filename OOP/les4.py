# НАСЛЕДОВАНИЕ

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"




class Line:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_line(self) -> int:  # -> int какой возвращается тип данных
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
        return self._width


class Rect:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw_rect(self) -> int:  # -> int какой возвращается тип данных
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
        return self._width


line = Line(Point(1, 2), Point(10, 20), "black", 8)
line.draw_line()

rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()

# DRY (Don't Repeat Yourself) - не повторяйся
