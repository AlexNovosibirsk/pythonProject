# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
tuple_ = 1, 2, 3
immutable_var = ([1, 2, 3], "str", -5, 5.7, True) + tuple_ # кортежи можно сложить
#   - Выполните операции вывода кортежа immutable_var на экран.
print(immutable_var) # ([1, 2, 3], 'str', -5, 5.7, True, 1, 2, 3)
print(immutable_var[0][1])
immutable_var[0][1] = 7 # список внутри кортежа можно менять
print(immutable_var) # ([1, 7, 3], 'str', -5, 5.7, True, 1, 2, 3)
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# tuple[1] = 3 #TypeError: 'tuple' object does not support item assignment
# кортеж неизменяемый тип - будет ошибка
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 3, 2, "Text", 0.5, (1, 2, 3)]
#   - Измените элементы списка mutable_list.
mutable_list[3] = "String"
mutable_list.append(-10.3)
# mutable_list[5][1] = 6 кортеж внутри списка менять нельзя
#   - Выведите на экран измененный список mutable_list.
print(mutable_list) # [1, 3, 2, 'String', 0.5, (1, 2, 3), -10.3]
# проверим типы данных коллекций
print(type(mutable_list)) #<class 'list'>
print(type(immutable_var)) #<class 'tuple'>



