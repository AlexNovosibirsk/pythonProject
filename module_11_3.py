"""
Интроспекция

Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты,
методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""

import requests
from pprint import pprint
import inspect
import sys


class SomeClass:
    attribute_0 = 12

    def __init__(self):
        self.attribute_1 = 123
        self.attribute_2 = "txt"
        self.attribute_3 = 12.0

    def some_metod_1(self):
        self.attribute_1 += 1

    def some_metod_2(self, txt):
        self.attribute_2 = txt

    @staticmethod
    def introspection_info(obj):
        dict_info = dict()

        str_ = str(type(obj))
        dict_info.update({'type': str_.split("\'")[1]})

        # Создадим два списка вызываемых и невызываемых атрибутов
        # Dunder-методы и атрибуты исключим из списков, так как их слишком много
        list_methods = [arg for arg in dir(obj)
                        if callable(getattr(obj, arg)) and arg.startswith('__') is False]
        dict_info.update({'methods': list_methods})

        list_attributes = [arg for arg in dir(obj)
                           if callable(getattr(obj, arg)) is not True and arg.startswith('__') is False]
        dict_info.update({'attributes': list_attributes})

        str_ = str(inspect.getmodule(obj))
        if str_ == "None":
            dict_info.update({'module': None})
        else:
            dict_info.update({'module': str_.split("\'")[1]})

        dict_info.update({'sizeof': sys.getsizeof(obj)})
        return dict_info


if __name__ == "__main__":

    someClass = SomeClass()
    result = someClass.introspection_info(someClass)
    # print(result)
    for item in result.items():
        print(item)


