"""
requests - запросить данные с сайта и вывести их в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.

pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение)
и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
"""

# Для исследования возьмем библиотеки pandas и matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# https://github.com/AlexNovosibirsk/pythonProject/blob/master/data.csv
class Explorer:

    def __init__(self):
        self.df = None
        try:
            self.df = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("FileNotFoundError")

    def describe(self):
        if self.df is not None:
            print(self.df.dtypes)  # выведем типы данных в таблице
            print(self.df.describe())  # и некоторые статистические данные

    def print_head(self, num):
        if self.df is not None:
            print(self.df.head(num))

    def print_tail(self, num):
        if self.df is not None:
            print(self.df.tail(num))

    def print_sort(self):  # Отсортируем по указанной колонке
        if self.df is not None:
            print(self.df.sort_values(by="Duration"))

# далее, используя библиотеку matplotlib, построим график и гистограмму по данным из data.csv
    def create_plot(self):  # построим график по одной из колонок (Duration) таблицы
        if self.df is not None:
            x = self.df.index.tolist()
            y = self.df["Duration"].values
            plt.plot(x, y, color='red', )
            plt.xlabel('Ось х')
            plt.ylabel('Ось y')
            plt.title('график')
            plt.show()

    def create_gist(self):  # также построим гистограмму
        if self.df is not None:
            plt.hist(self.df["Duration"], label="Duration")
            plt.xlabel("Ось х")
            plt.ylabel("Ось y")
            plt.legend()
            plt.show()


if __name__ == "__main__":
    exp = Explorer()
    exp.describe()
    exp.print_head(10)
    exp.print_sort()
    exp.create_plot()
    exp.create_gist()

# В данном примере представлена лишь малая часть возможностей исследуемых билиотек.
# Выбранные для изучения библиотеки являются мощными инструментами для анализа данных.
# Благодаря простому интерфейсу библиотек можно организовать необходимый анализ
# данных с последующим выводом результатов в виде графиков, гистограмм, круговых диаграмм...



# https://pythonru.com/biblioteki/pyplot-uroki (пригодится)
