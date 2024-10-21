"""
requests - запросить данные с сайта и вывести их в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение)
и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
"""

import pandas as pd
import matplotlib.pyplot as plt


class Explorer:

    def __new__(cls, *args, **kwargs):
        cls.df = None
        try:
            cls.df = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("FileNotFoundError")
        instance = super(Explorer, cls).__new__(cls)
        return instance

    def __init__(self):
        pass

    def describe(self):
        print(self.df.dtypes)  # выведем типы данных в таблице
        print(self.df.describe())  # и некоторые статистические данные

    def print_head(self, num):
        print(self.df.head(num))

    def print_tail(self, num):
        print(self.df.tail(num))

    def print_sort(self):
        pass

# далее, используя библиотеку matplotlib, построим график и гистограмму по данным из data.csv
    def create_plot(self):  # построим график по одной из колонок (Duration) таблицы
        x = self.df.index.tolist()
        y = self.df["Duration"].values
        plt.plot(x, y, color='red', )
        plt.xlabel('Ось х')
        plt.ylabel('Ось y')
        plt.title('график')
        plt.show()

    def create_gist(self):  # также построим гистограмму
        plt.hist(self.df["Duration"], label="Duration")
        plt.xlabel("Ось х")
        plt.ylabel("Ось y")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    exp = Explorer()
    exp.describe()
    exp.print_head(10)
    exp.create_plot()
    exp.create_gist()

# В данном примере представлена лишь малая часть возможностей исследуемых билиотек.
# Выбранные для изучения библиотеки являются мощными инструментами для анализа данных.
# Благодаря простому интерфейсу библиотек можно организовать необходимый анализ
# данных с последующим выводом результатов в виде графиков, гистограмм, круговых диаграмм...

# https://pythonru.com/biblioteki/pyplot-uroki