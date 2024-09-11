"""
Задание "Они все так похожи":
"""

from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, RGB, *sides):
        self.__sides = []
        self.__color = []
        self.set_color(RGB[0], RGB[1], RGB[2])
        if len(list(sides)) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    def __is_valid_color(self, r, g, b):
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

    def __init__(self, RGB, *one_side_cube):
        sides = []
        for s in one_side_cube:
            sides.append(s)
        sides *= self.sides_count
        super().__init__(RGB, *sides)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, RGB, *sides):
        super().__init__(RGB, *sides)

    def get_square(self):
        sides = self.get_sides()
        p = (sides[0] + sides[1] + sides[2]) / 2
        S = sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return S


class Circle(Figure):
    sides_count = 1

    def __init__(self, RGB, *L):
        super().__init__(RGB, *L)
        self.__radius = 0.0

    def get_square(self):
        L = self.get_sides()
        self.__radius = L[0] / (2 * pi)
        S = pi * self.__radius ** 2
        return S


cube = Cube((115, 127, 195),9)
triangle = Triangle((21, 153, 89), 7, 5, 6)
circle = Circle((27, 180, 45), 19)

print(f"cube:     RGB={cube.get_color()},sides={cube.get_sides()}{cube.sides_count},P={len(cube)},V={cube.get_volume()}")
print(f"triangle: RGB={triangle.get_color()},sides={triangle.get_sides()}{triangle.sides_count},P={len(triangle)},S={triangle.get_square()}")
print(f"circle:   RGB={circle.get_color()},sides={circle.get_sides()}{circle.sides_count},P={len(circle)},S={circle.get_square()}")
print("---------------------------")
cube.set_color(123, 123, 235)
cube.set_color(123, 423, 235)
cube.set_sides(8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8)

cube.set_sides(10)
triangle.set_sides(8, 9, 11)
circle.set_sides(58)

print(f"cube:     RGB={cube.get_color()},sides={cube.get_sides()}{cube.sides_count},P={len(cube)},V={cube.get_volume()}")
print(f"triangle: RGB={triangle.get_color()},sides={triangle.get_sides()}{triangle.sides_count},P={len(triangle)},S={triangle.get_square()}")
print(f"circle:   RGB={circle.get_color()},sides={circle.get_sides()}{circle.sides_count},P={len(circle)},S={circle.get_square()}")
