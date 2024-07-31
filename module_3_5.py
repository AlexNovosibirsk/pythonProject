
"""
Задача "Рекурсивное умножение цифр":
Напиши функцию get_multiplied_digits,
которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
"""


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print(get_multiplied_digits(40203))
