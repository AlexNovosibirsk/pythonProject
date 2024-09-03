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

    def get_products(self):
        txt = ""
        try:
            file = open(self.__file_name, "r")
            try:
                txt = file.read()
            finally:
                file.close()
        except FileNotFoundError:
            print("file not found")
        except:
            print("the file cannot be read")
        return txt

    def add(self, *products):
        str_product = self.get_products()
        with open(self.__file_name, "a") as file:
            for pr in products:
                if pr.name in str_product:
                    print(f"Продукт {pr.name}, {pr.weight}, {pr.category} уже есть в магазине")
                else:
                    file.write(str(pr) + "\n")



def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print("p2->", p2)
    s1.add(p1, p2, p3)
    print(s1.get_products())


if __name__ == "__main__":
    main()
else:
    raise SystemExit("Это основной файл")

"""
p2-> Spaghetti, 3.4, Groceries
file not found
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

p2-> Spaghetti, 3.4, Groceries
Продукт Potato, 50.5, Vegetables уже есть в магазине
Продукт Spaghetti, 3.4, Groceries уже есть в магазине
Продукт Potato, 5.5, Vegetables уже есть в магазине
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables
"""