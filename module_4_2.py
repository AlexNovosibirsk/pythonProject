
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function() # Я в области видимости функции test_function
#inner_function() #NameError: name 'inner_function' is not defined.
# внутреннюю функцию снаружи запустить не удалось

