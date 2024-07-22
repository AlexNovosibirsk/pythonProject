"""
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0
"""

"""
определим ввод целых чисел в виде функции с простой проверкой на 
предмет случайных символов в цифровой строке (123jkfdh5445) 
"""
def input_nums(txt):
    while True:
        num_str = input(txt)
        if num_str.isdigit():
            return int(num_str)


def compare_nums():
    if first == second and first == third:
        return 3
    elif (first == second or
          first == third or
          second == third):
        return 2
    elif first != second and first != third:
        return 0


first = input_nums("Первое число:")
second = input_nums("Второе число:")
third = input_nums("Третье число:")
print("Результат: ", compare_nums())
# Первое число:456hdK
# Первое число:12
# Второе число:34
# Третье число:12
# Результат:  2