"""
Задача "Изменять нельзя получать"
"""


class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner="", model="", color="", engine_power=115):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def set_color(self, new_color):
        for i in self.__COLOR_VARIANTS:
            if i.upper() == new_color.upper():
                self.__color = new_color
                return
        print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# print(vehicle1.__dict__)
# Изначальные свойства
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print("--------------------------")
# Проверяем что поменялось
vehicle1.print_info()

"""
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: blue
Владелец: Fedos
Нельзя сменить цвет на Pink
--------------------------
Модель: Toyota Mark II
Мощность двигателя: 500
Цвет: BLACK
Владелец: Vasyok
"""

