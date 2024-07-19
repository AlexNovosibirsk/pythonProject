# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
my_dict = {"Пушкин": 1799, "Толстой": 1828, "Достоевский": "1821"}
#   - Выведите на экран словарь my_dict.
print(my_dict)  #{'Пушкин': 1799, 'Толстой': 1828, 'Достоевский': '1821'}
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print(my_dict["Пушкин"])
print(my_dict.get("Тургенев", "Тургенев в списке отсутствует"))  #None
# более практичное применение: проверим, есть ли в коллекции  Достоевский
result = my_dict.get("Достоевский")
print("result: ", result, type(result))  #result:  1821 <class 'str'>
if result is None:
    print("None")
else:
    print(result)

#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict["Лермонтов"] = 1814
my_dict["Некрасов"] = 1821
# или
my_dict.update({"Лермонтов": 1814, "Некрасов": 1821})  #данная строка не возымеет действия - эти пары уже добавлены
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
name = input("Name: ")#name = "Достоевский"
if my_dict.get(name) is not None:
    storage = my_dict.pop(name)  # или del my_dict["Достоевский"]
    print(storage)
#   - Выведите на экран словарь my_dict.
print(my_dict)  #{'Пушкин': 1799, 'Толстой': 1828, 'Лермонтов': 1814, 'Некрасов': 1821}


# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 2, 3, 4, 5, 53, 21, 1, 4, 5, 6, 7, 5, 3, 3, 0, 0, 3, 2, 21}
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print(my_set) # {0, 1, 2, 3, 4, 5, 6, 7, 53, 21}
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.update({111, 222})
my_set.add(100)
#   - Удалите один любой элемент из множества my_set.
print(my_set.pop())# удалим нулевой элемент и покажем его
# или
my_set.remove(2)# и еще один удалим
my_set.discard(555)
#   - Выведите на экран измененное множество my_set.
print(my_set)#{1, 3, 4, 6, 7, 100, 111, 53, 21, 222}