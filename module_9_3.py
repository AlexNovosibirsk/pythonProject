"""

"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# В переменную first_result запишите генераторную сборку,
# которая высчитывает разницу длин строк из списков first и second,
# если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
first_result = (abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) != len(j))
print(list(first_result))

# В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
