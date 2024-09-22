"""
Задача "Функциональное разнообразие":
"""

"""
Lambda-функция:
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Здесь ? - место написания lambda-функции.
Результатом должен быть список совпадения букв в той же позиции:
[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
Где True - совпало, False - не совпало.
"""

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

"""
Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий 
неограниченное количество данных любого типа.
Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
Функция get_advanced_writer возвращает функцию write_everything.
"""


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for i in data_set:
                file.write(str(i) + "\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 0.95, {"A":5,"B":7})

"""
Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово 
из words и возвращать его.
"""

from random import choice


class MysticBall:
    words = list()

    def __init__(self, *args):
        self.words = args

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

