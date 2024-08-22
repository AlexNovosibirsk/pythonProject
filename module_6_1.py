"""
Задача "Съедобное, несъедобное":
"""


class Animal:
    def __init__(self, name=""):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name  # название животного.

    def eat(self, food):
        if food.edible:
            self.alive = True
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            self.fed = False
            print(f"{self.name} не стал есть {food.name}")


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

"""
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True
"""
