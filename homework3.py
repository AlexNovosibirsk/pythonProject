# идентификатор(переменная) name указывает на обьект класса str,
# следовательно, к строке применимы методы класса str, например:
name = "Василий ИВАНОВx".title().strip("x")
Name = "Tom" # это другая переменная, хотя звучит также
print("Name:", name)
age = 37
print("Age: ", age)
age += 5 #age = age + 5
print("New Age: ", age)
is_student = True
print("Is Student: ", is_student)

# при данном сочетании определений компилятор выдаст предупреждение
age = 17
age = 15 # Redeclared 'age' defined above without usage

