"""
Задача "Счётчик вызовов":
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки,
строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True,
если строка находится в этом списке, False - если отсутствует.
Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
"""

calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()
    return len(str_), str_.lower(), str_.upper()


def is_contains(str_, list_):
    count_calls()
    for i in list_:
        if i.upper() == str_.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

"""
(8, 'capybara', 'CAPYBARA')
(10, 'armageddon', 'ARMAGEDDON')
True
False
4
"""
