"""
Задание "Они все так похожи":

Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube,
объекты которых будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть
написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все
стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

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

Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""
import math


class Figure:
    sides_count = 0  # Атрибуты класса Figure

    def __init__(self, *args):
        self.__sides = []  # (список сторон(целые числа))
        match self.sides_count:
            case 12:
                for i in range(self.sides_count):
                    self.__sides.append(args[1])
            case 1:
                self.__sides.append(args[1])
            case 3:
                for i in range(self.sides_count):
                    self.__sides.append(args[i+1])

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            for i in range(len(self.__sides)):
                self.__sides[i] = new_sides[i]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):

        return True


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args):
        super().__init__(*args)

    def get_volume(self):
        side = self.get_sides()
        return side[0]**3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args):
        super().__init__(*args)

    def get_square(self):
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2])/2
        S = math.sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))
        return S


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args):
        self.__radius = None  # рассчитать исходя из длины окружности (одной единственной стороны).
        super().__init__(*args)

    def get_square(self):  # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        L = self.get_sides()
        self.__radius = L[0] / (2 * math.pi)
        S = math.pi * self.__radius**2
        return S


cube = Cube((222, 35, 130), 4)
triangle = Triangle((115, 127, 195), 15, 18, 12)
circle = Circle((27, 180, 45), 19)
print(cube.get_sides())
print(triangle.get_sides())
print(circle.get_sides())

print(cube.get_volume())
print(circle.get_square())
print(triangle.get_square())
# Проверка на изменение сторон:
# cube.set_sides(5, 3, 12, 4, 5)  # Не изменится
# print(cube.get_sides())
# cube.set_sides(8,8,8,8,8,8,8,8,8,8,8,8)
# print(cube.get_sides())
# triangle.set_sides(5, 3, "12")
# circle.set_sides(81)
# print(triangle.get_sides())
# print(circle.get_sides())
# for i in args:
#     if isinstance(i, tuple):
#         for color in i:
#             self._color.append(color)
#     if isinstance(i, int):
#         for k in range(self.sides_count):
#             self.__sides[k] = i
