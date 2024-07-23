"""
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value,
которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов,
заполненную значениями value и возвращать эту матрицу в качестве результата работы.
"""


def get_matrix(n, m, value):

    matrix = []
    row_list = []
# В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список.
# подразумевается любой аргумент
    if n <= 0 or m <= 0 or value <= 0:
        return matrix

    for i in range(n):
        row_list.clear()
        for j in range(m):
            row_list.append(value)
        matrix .append(row_list)

    return matrix


result1 = get_matrix(2, 5, -10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(4, 2, 3)
print(result1)
print(result2)
print(result3)
print(result4)

# []
# [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
# [[13, 13], [13, 13], [13, 13], [13, 13]]
# [[3, 3], [3, 3], [3, 3], [3, 3]]