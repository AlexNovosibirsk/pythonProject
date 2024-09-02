"""
Задача "Учёт товаров"
"""


class Product:
    def __init__(self, *args):
        self.name = args[0]  # название продукта(строка).
        self.weight = args[1]  # общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = args[2]  # категория товара (строка).

    def __str__(self):  # возвращает строку в формате '<название>, <вес>, <категория>'.
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    # get_products считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами из файла __file_name
    def get_products(self):
        txt = ""
        try:
            file = open(self.__file_name, "r")
        except FileNotFoundError:
            print("file not found")
            return txt
        else:
            txt = file.read()
            file.close()
        finally:
            return txt

    # принимает неограниченное количество объектов класса Product.
    # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'
    def add(self, *products):
        str_product = self.get_products()
        file = open(self.__file_name, "a")
        for pr in products:
            if pr.name in str_product:
                print(f"Продукт {pr.name}, {pr.weight}, {pr.category} уже есть в магазине")
            else:
                file.write(str(pr) + "\n")
        file.close()


def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)
    s1.add(p1, p2, p3)
    print(s1.get_products())


if __name__ == "__main__":
    main()
else:
    raise SystemExit("Это основной файл")
