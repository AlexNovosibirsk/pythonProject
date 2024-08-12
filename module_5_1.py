"""
Задача "Developer - не только разработчик"
"""

class House:
    def __init__(self, name="Unknown", number_of_floors=10):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"Такого этажа не существует \"{self.name}\"")
            return
        for i in range(1, new_floor+1):
            print(i, self.name)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House()
h4 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(12)
h4.go_to(7)

"""
1 ЖК Горский
2 ЖК Горский
3 ЖК Горский
4 ЖК Горский
5 ЖК Горский
Такого этажа не существует "Домик в деревне"
Такого этажа не существует "Unknown"
1 ЖК Эльбрус
2 ЖК Эльбрус
3 ЖК Эльбрус
4 ЖК Эльбрус
5 ЖК Эльбрус
6 ЖК Эльбрус
7 ЖК Эльбрус
"""