"""
"Пространство имен."
"""


# области видимости подразделяются на следующие:
# локальная
# объемлющая
# глобальная
# встраиваемая  import...

def test_function():
    # Объемлющая область видимости появляется тогда,
    # когда у нас одна функция находится внутри другой.

    x = 6

    def inner_function():
        nonlocal x # Х будет изменена во внутренней функции
        x = 5
        print("Я в области видимости функции test_function")

    inner_function()
    return x

print(test_function())  # Я в области видимости функции test_function
#inner_function() #NameError: name 'inner_function' is not defined.
# внутреннюю функцию снаружи запустить не удалось
