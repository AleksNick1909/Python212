
class Student:
    def __init__(self):
        self.rom = "Roman"
        self.vl = "Vladimir"
        self.lg = self.Comp()

    class Comp:
        def __init__(self):
            self.name = "HP, i7, 16"

        def display1(self):
            print(outer.rom, "=>", self.name)

        def display2(self):
            print(outer.vl, "=>", self.name)


outer = Student()
g = outer.lg
g.display1()
g.display2()

