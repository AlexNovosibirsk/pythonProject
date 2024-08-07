
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
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function() # Я в области видимости функции test_function
#inner_function() #NameError: name 'inner_function' is not defined.
# внутреннюю функцию снаружи запустить не удалось

