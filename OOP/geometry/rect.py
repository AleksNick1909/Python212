class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


# print(__name__)  # __main__  запуск программы с этого документа

# geometry.rect  - запустили документ как модуль в start.py

__author__ = "Aleks"
if __name__ == '__main__':
    print(f"Modul {__name__} ({__author__})")
