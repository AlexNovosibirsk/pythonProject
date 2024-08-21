"""
Задача "Мифическое наследование":


Примечания:
Будьте внимательней, когда вызываете методы классов родителей в классе
наследнике при множественном наследовании: при обращении через super()
методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat",
т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
"""


class Horse:
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        self.sound = Eagle.sound
        """
        Так как атрибут sound присутствует и в Horse и в Eagle, то Pegasus возьмет sound
        из первого же класса по списку наследования в котором он имеется.
        В строке self.sound = Eagle.sound мы точно определяем от какого базового класса Pegasus 
        получит sound, независимо от порядка наследования. Нам нужен sound из Eagle.
        Иначе получим sound из Horse.
        """
        print(self.sound)


pegasus = Pegasus()
print(pegasus.get_pos())
pegasus.move(10, 15)
print(pegasus.get_pos())
pegasus.move(-5, 20)
print(pegasus.get_pos())
pegasus.voice()
print(Pegasus.mro())

"""
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat
"""