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

import inspect
import sys


class SomeClass:
    attribute_0 = 12

    def __init__(self):
        self.attribute_1 = 123
        self.attribute_2 = "txt"
        self.attribute_3 = 12.0

    def some_method_1(self):
        self.attribute_1 += 1

    def some_method_2(self, txt):
        self.attribute_2 = txt

    @staticmethod
    def introspection_info(obj):
        dict_info = dict()

        dict_info['type'] = type(obj).__name__

        # Dunder-методы исключим, так как их слишком много
        dict_info['methods'] = [m for m in dir(obj) if callable(getattr(obj, m)) and not m.startswith('__')]
        dict_info['attributes'] = [a for a in dir(obj) if not callable(getattr(obj, a)) and not a.startswith('__')]

        module = inspect.getmodule(obj)
        dict_info['module'] = module.__name__ if module else None

        dict_info['sizeof'] = sys.getsizeof(obj)

        dict_info['id'] = id(obj)

        return dict_info


if __name__ == "__main__":
    someClass = SomeClass()
    result = SomeClass.introspection_info(someClass)
    for key, value in result.items():
        print(f"{key}: {value}")


