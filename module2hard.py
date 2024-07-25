"""
Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки)
с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом,
а второе было всегда пустым.
К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус,
где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
Во вторую вставку нужно было написать те пары чисел друг за другом,
чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)

Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)

К сожалению, у вас не так много времени, чтобы подбирать пароль вручную,
шипы сверху уже движутся на вас (обожаю клише),
тем более числа в первой вставке будут попадаться случайно.

Составьте алгоритм, используя циклы,
чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный пароль result,
для одного введённого числа.
"""


def input_nums():
    while True:
        try:
            num = int(input("num: "))
        except ValueError:
            print('Это не число.')
        else:
            print('Всё хорошо.')
            if num < 3:
                num = 3
            elif num > 20:
                num = 20
            return num
        finally:
            pass
        # print('Я обязательно закрыл файл или сокет')


def password_creator(n):
    result_str = ""
    for part_1 in range(1, nums):
        for part_2 in range(1, nums):
            # List.clear()
            if nums % (part_1 + part_2) == 0 and part_1 < part_2:
                result_str += str(part_1) + str(part_2)
                # List.append(part_1)
                # List.append(part_2)
                # List.sort()
                # pair.update({List[0]: List[1]})
    return result_str


while True:
    nums = input_nums()
    result = password_creator(nums)
    print(nums, result)








"""
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