"""
Задача "Магические здания"

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
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

    def __str__(self): # возвращает пользователю читаемый текст об объекте
        return f'Название: {self.name}, количество этажей {self.number_of_floors}'

    def __len__(self): # определим __len__ для подсчета чего-либо в пользовательском типе
        return self.number_of_floors # возвращается целое большее, либо равное нулю

    def __repr__(self):# переопределим также метод __repr__
        return f"{self.__class__}: {self.name}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House()

# __str__
print(h1)   # так как метод __str__ определен в классе House, то будет вызван именно он,
            # иначе будет вызываться  переопределенный __repr__
print(str(h1))# метод __str__ можно вызвать и так
print(h2)
print(h3)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))

print(repr(h1))
"""
Название: ЖК Эльбрус, количество этажей 10
Название: ЖК Эльбрус, количество этажей 10
Название: ЖК Акация, количество этажей 20
Название: Unknown, количество этажей 10
10
20
10
<class '__main__.House'>: ЖК Эльбрус
"""















