"""
Задание "Раз, два, три, четыре, пять .... Это не всё?":
Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)
"""

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


stack_ = [] # в качестве стека используется список, но лучше использовать
            # настоящий стек или очередь, что было проделано в закомментированном ниже коде
def calculate_structure_sum(*args):
    summ = 0
    for data in args[0]:
        if isinstance(data, int):   # подсчитываем элементарные типы, которые нам нужны
            summ += data
        elif isinstance(data, str):
            summ += len(data)
        else:
            stack_.append(data) # сохраняем все не распакованные коллекции

        # if (isinstance(data, list) or isinstance(data, dict) or
        #         isinstance(data, tuple) or isinstance(data, set)):
        #     stack.append(data)

    for i in range(len(stack_)):
        collection = stack_.pop() # берем одну из коллекций и отправляем на очередную распаковку
        print(collection) # посмотрим что будем отдавать далее
        if isinstance(collection, list) or isinstance(collection, tuple) or isinstance(collection, set):
            return summ + calculate_structure_sum(collection)
        if isinstance(collection, dict): # словарь надо дополнительно преобразовать
            return summ + calculate_structure_sum(set(collection.items()))
    return summ


print(calculate_structure_sum(data_structure)) # 99

""" 
((), [{(2, 'Urban', ('Urban2', 35))}])
[{(2, 'Urban', ('Urban2', 35))}]
{(2, 'Urban', ('Urban2', 35))}
(2, 'Urban', ('Urban2', 35))
('Urban2', 35)
()
(6, {'cube': 7, 'drum': 8})
{'cube': 7, 'drum': 8}
('cube', 7)
('drum', 8)
{'a': 4, 'b': 5}
('a', 4)
('b', 5)
[1, 2, 3]
99
"""




# from queue import Queue
# q = Queue()
# from collections import deque
# stack = deque()
#
#
# def calculate_structure_sum_2(*args):
#     summ = 0
#     item = args[0]
#     for data in item:
#         if isinstance(data, int):
#             summ += data
#         elif isinstance(data, str):
#             summ += len(data)
#         else:
#             q.put(data)
#
#     while not q.empty():
#         collection = q.get()
#         #print(collection)
#         if isinstance(collection, list) or isinstance(collection, tuple):
#             return summ + calculate_structure_sum_2(collection)
#         if isinstance(collection, dict):
#             return summ + calculate_structure_sum_2(set(collection.items()))
#         if isinstance(collection, set):
#             return summ + calculate_structure_sum_2(list(collection))
#     return summ
#
#
# print(calculate_structure_sum_2(data_structure))
#
# def calculate_structure_sum_3(*args):
#     summ = 0
#     item = args[0]
#     for data in item:
#         if isinstance(data, int):
#             summ += data
#         elif isinstance(data, str):
#             summ += len(data)
#         else:
#             stack.append(data)
#
#     for i in range(len(stack)):
#         collection = stack.pop()
#         #print(collection)
#         if isinstance(collection, list) or isinstance(collection, tuple):
#             return summ + calculate_structure_sum_3(collection)
#         if isinstance(collection, dict):
#             return summ + calculate_structure_sum_3(set(collection.items()))
#         if isinstance(collection, set):
#             return summ + calculate_structure_sum_3(list(collection))
#     return summ
#
#
# print(calculate_structure_sum_3(data_structure))
