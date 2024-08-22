"""
Задача "Съедобное, несъедобное":
"""


class Animal:
    def __init__(self, name=""):
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name  # название животного.


class Mammal(Animal):
    def eat(self, food):
        print(food.Edible)
        if food.get_edible():
            self.alive = True
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            self.fed = False
            print(f"{self.name} не стал есть {food.name}")


class Predator(Animal):
    def eat(self, food):
        print(food.Edible) # 2. проверим состояние унаследованного атрибута класса Plant,
        # но пользоваться будем атрибутами объекта
        if food.get_edible():
            self.alive = True
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            self.fed = False
            print(f"{self.name} не стал есть {food.name}")


class Plant:
    Edible = "False" # 1. объявим атрибут класса и поменяем его состояние в наследниках

    def __init__(self, name):
        print(f"Конструктор Plant для {self.__class__}")
        self.edible = True  # съедобность
        self.name = name  # название растения

    def get_edible(self):  # переопределяемый в наследниках геттер
        #  нужен в случае если атрибуты класса Plant были бы protected,
        #  но они public из-за этих строк:
        #  print(f"{self.name} не стал есть {food.name}")   print(f"{self.name} съел {food.name}")
        raise NotImplementedError("get_edible() должен быть переопределен")


class Flower(Plant):

    def __init__(self, name):
        super().__init__(name)
        # так как отдельного метода не предусматривается для изменения состояния self.edible
        # то self.edible будет меняться в конструкторе наследника
        # базовый класс так же имеет свой конструктор, который нужно вызвать, поэтому
        # делегируем наследнику вызов инициализатора базового класса (super().__init__)
        self.edible = False  # съедобность
        if self.Edible == "False":  # проверим, что унаследовали атрибут класса Edible из Plant
            self.Edible = "Не съедобно"  # и изменим его состояние 
            
    def get_edible(self):
        return self.edible


class Fruit(Plant):

    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # съедобность
        if self.Edible == "False":
            self.Edible = "Съедобно"
            
    def get_edible(self):
        return self.edible


flower = Flower('Цветик семицветик')
fruit = Fruit('Заводной апельсин')
"""
Конструктор Plant для <class '__main__.Flower'>
Конструктор Plant для <class '__main__.Fruit'>
"""
print(fruit.__dict__)
print(flower.__dict__)
"""
{'edible': True, 'name': 'Заводной апельсин'}
{'edible': False, 'name': 'Цветик семицветик'}
"""
predator = Predator('Волк с Уолл-Стрит')
mammal = Mammal('Хатико')

mammal.eat(fruit)
predator.eat(flower)
"""
Хатико съел Заводной апельсин
Волк с Уолл-Стрит не стал есть Цветик семицветик
"""
print(mammal.__dict__)
print(predator.__dict__)
"""
{'alive': True, 'fed': True, 'name': 'Хатико'}
{'alive': False, 'fed': False, 'name': 'Волк с Уолл-Стрит'}
"""


