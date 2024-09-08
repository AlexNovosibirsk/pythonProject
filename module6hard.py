"""
Задание "Они все так похожи":
"""

from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []  # список сторон (целые числа)
        self.__color = []  # список цветов в формате RGB
        self.filled = False  # закрашенный, bool

    def init_sides_colors(self, num_sides, *args):
        for i in range(len(args)):
            if isinstance(args[i], int) and args[i] >= 0:
                self.__sides.append(args[i])
            if isinstance(args[i], tuple):
                for tuple_arg in args[i]:
                    if isinstance(tuple_arg, int) and 0 <= tuple_arg < 256:
                        self.__color.append(tuple_arg)
        if len(self.__color) != 3:
            self.__color.clear()
            self.__color = [0, 0, 0]
        if len(self.__sides) != num_sides:
            self.__sides.clear()
            self.__sides = [1] * num_sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    @staticmethod
    def __is_valid_color(r, g, b):
        if (isinstance(r, int) and 0 <= r <= 255
                and isinstance(g, int) and 0 <= g <= 255
                and isinstance(b, int) and 0 <= b <= 255):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        else:
            for side in new_sides:
                if not isinstance(side, int) or side <= 0:
                    return False
        return True

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __len__(self):
        return sum(self.__sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__()
        self.init_sides_colors(1, *args)
        sides_cube = self.get_sides()
        if len(sides_cube) == 1:  # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
            sides_cube *= self.sides_count

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__()
        self.init_sides_colors(self.sides_count, *args)

    def get_square(self):
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        S = sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return S


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        self.__radius = 0.0  # рассчитать исходя из длины окружности (одной единственной стороны).
        super().__init__()
        self.init_sides_colors(self.sides_count, *args)

    def get_square(self):  # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        L = self.get_sides()
        self.__radius = L[0] / (2 * pi)
        S = pi * self.__radius ** 2
        return S


cube = Cube((115, 127, 195), 6)
triangle = Triangle(5, (21, "x", 89), 7, 5.5, "txt", 6, (53,))
circle = Circle((27, 180, 45), 19)

print(f"cube:     RGB={cube.get_color()},sides={cube.get_sides()}{cube.sides_count},P={len(cube)},V={cube.get_volume()}")
print(f"triangle: RGB={triangle.get_color()},sides={triangle.get_sides()}{triangle.sides_count},P={len(triangle)},S={triangle.get_square()}")
print(f"circle:   RGB={circle.get_color()},sides={circle.get_sides()}{circle.sides_count},P={len(circle)},S={circle.get_square()}")
print("---------------------------")
cube.set_color(123, 123, 235)
cube.set_color(123, 423, 235)
# по условию задачи для куба надо передавать все 12 сторон
# причем надо соблюдать чтобы все числа были между собой равны,
# хотя для куба можно было бы задавать одну сторону
cube.set_sides(8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8)

cube.set_sides(10)
triangle.set_sides(8, 9, 11)
circle.set_sides(58)

print(f"cube:     RGB={cube.get_color()},sides={cube.get_sides()}{cube.sides_count},P={len(cube)},V={cube.get_volume()}")
print(f"triangle: RGB={triangle.get_color()},sides={triangle.get_sides()}{triangle.sides_count},P={len(triangle)},S={triangle.get_square()}")
print(f"circle:   RGB={circle.get_color()},sides={circle.get_sides()}{circle.sides_count},P={len(circle)},S={circle.get_square()}")


