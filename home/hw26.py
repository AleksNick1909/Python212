class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise AssertionError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        return Clock(self.sec % other.sec)


c1 = Clock(600)
c2 = Clock(200)
print("c1:", c1.get_format_time())
c1 = c1 - c2
print("c1 - c2:", c1.get_format_time())

c1 = Clock(600)
c2 = Clock(200)
c1 = c1 * c2
print("c1 * c2:", c1.get_format_time())

c1 = Clock(600)
c2 = Clock(200)
c1 = c1 // c2
print("c1 // c2:", c1.get_format_time())

c1 = Clock(600)
c2 = Clock(200)
c1 = c1 % c2
print("c1 % c2:", c1.get_format_time())

c1 = Clock(600)
c2 = Clock(200)
c1 -= c2
print("c1 -= c2:", c1.get_format_time())

c1 *= c2
print("c1 *= c2:", c1.get_format_time())

c1 //= c2
print("c1 //= c2:", c1.get_format_time())

c1 %= c2
print("c1 %= c2:", c1.get_format_time())
