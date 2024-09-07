"""
Задание "Они все так похожи":


Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
значений перед установкой нового цвета.
Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).

Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
то не изменять, в противном случае - менять.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все
стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.

Метод __len__ должен возвращать периметр фигуры.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""

import math

class Figure:
    sides_count = 0          # Атрибут класса Figure

    def __init__(self):
        self.__sides = []    # список сторон (целые числа)
        self.__color = []    # список цветов в формате RGB
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

# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных
# значений перед установкой нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def set_color(self, r, g, b):
        if self.__is_valid_color(*(r, g, b)):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_color(*colors):
        for c in colors:
            if not isinstance(c, int) or c < 0 or c > 255:
                return False
        return True

# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
# то не изменять, в противном случае - менять.
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все
# стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    
    
    # Метод set_sides для объекта Cube должен принимать все 12 сторон?  cube.set_sides(8,8....8)(12) 
    # или для куба достаточно передавать одно число? cube.set_sides(8) как при инициализации. 
    # судя по ТЗ, задавать стороны куба надо так - cube.set_sides(8,8....8)(12) , тогда все 12 чисел дожны быть равны между собой
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            pass

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
        Perimetr = 0
        for side in self.__sides:
            Perimetr += side
        return Perimetr


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
        S = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return S


class Circle(Figure):
    sides_count = 1
    __radius = 0.0  # рассчитать исходя из длины окружности (одной единственной стороны).

    def __init__(self, *args):
        super().__init__()
        self.init_sides_colors(self.sides_count, *args)

    def get_square(self):  # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        L = self.get_sides()
        self.__radius = L[0] / (2 * math.pi)
        S = math.pi * self.__radius ** 2
        return S


cube = Cube((115, 127, 195), 7)
triangle = Triangle(5, (21, "x", 89), 7, 5.5, "txt", 6, (53,))
circle = Circle((27, 180, 45), 19)

print(f"cube:     RGB={cube.get_color()},sides={cube.get_sides()}{cube.sides_count},P={len(cube)},V={cube.get_volume()}")
print(f"triangle: RGB={triangle.get_color()},sides={triangle.get_sides()}{triangle.sides_count},P={len(triangle)},S={triangle.get_square()}")
print(f"circle:   RGB={circle.get_color()},sides={circle.get_sides()}{circle.sides_count},P={len(circle)},S={circle.get_square()}")
print("---------------------------")
cube.set_color(123, 123, 235)

cube.set_sides(8)
triangle.set_sides(8, 9, 11)
circle.set_sides(58)

# cube.set_sides(5, 3, 12, 4, 5)  # Не изменится
# cube.set_sides(18)
# triangle.set_sides(5, 3, "12")
# circle.set_sides(56)
