"""
Задача "Нужно больше этажей"
"""


class House:
    def __init__(self, name="Unknown", number_of_floors=10):
        self.number_of_floors = number_of_floors
        self.name = name
        # print("Init")

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"Такого этажа не существует \"{self.name}\"")
            return
        for i in range(1, new_floor+1):
            print(i, self.name)
    def __str__(self):
        return f'Название: {self.name}, количество этажей {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    def __iadd__(self, value):
        return self.__add__(self)
    def __radd__(self, value):
        return self.__add__(self)
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

"""
Название: ЖК Эльбрус, количество этажей 10
Название: ЖК Акация, количество этажей 20
False
Название: ЖК Эльбрус, количество этажей 20
True
Название: ЖК Эльбрус, количество этажей 20
Название: ЖК Акация, количество этажей 20
False
True
False
True
False
"""




