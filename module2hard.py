from multipledispatch import dispatch
"""
Задание "Слишком древний шифр":

Составьте алгоритм, используя циклы,
чтобы в независимости от введённого числа n (от 3 до 20) 
программа выдавала нужный пароль result для одного введённого числа.
"""


def input_nums():
    while True:
        try:
            num = int(input("num: "))
        except ValueError:
            print('Это не число.')
        else:
            print('Число принято.')
            if num < 3:
                num = 3
            elif num > 20:
                num = 20
            return num
        finally:
            pass
        # print('Я обязательно закрыл файл или сокет')


# сначала реализуем password_creator в развернутом виде
# для понимания сути происходящего
@dispatch(int)
def password_creator(n):
    result_str = ""
    for part_1 in range(1, n):
        for part_2 in range(1, n):
            if n % (part_1 + part_2) == 0:
                if part_1 == part_2: # отсекаем пары с равными частями, в ответах они отсутствуют
                    continue
                if part_1 < part_2: # отсекаем пары уже имеющиеся, но зеркально отображенные
                    result_str += str(part_1) + str(part_2)
    return result_str # результат представим строкой


# упростим функцию, имя оставим тем же
@dispatch(int, int)
def password_creator(n, x):
    result_str = ""
    for part_1 in range(1, n):
        for part_2 in range(1, n):
            if n % (part_1 + part_2) == 0 and part_1 < part_2:
                result_str += str(part_1) + str(part_2)
    return result_str


while True:
    nums = input_nums()
    result = password_creator(nums)
    print(f'password for {nums} -> {result}')
    print(password_creator(nums, 0))


"""
num: 12
Число принято.
password for 12 -> 12131511124210394857
12131511124210394857
"""


""" для проверки
3 - 12
4 - 13
5 - 1423
6 - 121524
7 - 162534
8 - 13172635
9 - 1218273645
10 - 141923283746
11 - 11029384756
12 - 12131511124210394857
13 - 112211310495867
14 - 1611325212343114105968
15 - 1214114232133124115106978
16 - 1317115262143531341251161079
17 - 11621531441351261171089
18 - 12151811724272163631545414513612711810
19 - 118217316415514613712811910
20 - 13141911923282183731746416515614713812911
"""