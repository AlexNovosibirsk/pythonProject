# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразуем множество строк в список строк
students = list(students)
print(students)
#students_list = list(students)
# отсортируем список
students.sort()
print(students)
#['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
par = {}

# циклично расчитаем среднее и заполним коллекцию пар
for v in range(len(students)):
    average = sum(grades[v])/len(grades[v])
    par.update({students[v]: average})

print(par)
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}