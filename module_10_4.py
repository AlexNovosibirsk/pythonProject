"""
Задача "Потоки гостей в кафе":
"""
from queue import Queue
from threading import Thread
from time import sleep
from random import randint


class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Cafe:
    def __init__(self, *table: list):
        self.queue = Queue()
        self.tables = table

    def search_free_table(self):
        free_index, cnt_free_table = None, 0

        for j in range(len(self.tables)):
            if self.tables[j].guest is None:
                cnt_free_table += 1

        for j in range(len(self.tables)):
            if self.tables[j].guest is None:
                free_index = j
                break

        return free_index, cnt_free_table

    def guest_arrival(self, *guest: Guest):
        for gst in guest:
            free_table_index, x = self.search_free_table()
            if free_table_index is not None:
                self.tables[free_table_index].guest = gst
                gst.start()
                print(f"{gst.name} сел за стол номер {self.tables[free_table_index].number}")
            else:
                self.queue.put(gst)
                print(f"{gst.name} в очереди")

    def discuss_guests(self):
        cnt_free_tables = int()
        while True:
            sleep(0.5)
            for i in range(len(self.tables)):
                if self.tables[i].guest is not None and not self.tables[i].guest.is_alive():
                    print(f"{self.tables[i].guest.name} покушал и ушёл. Стол номер {self.tables[i].number} свободен")
                    self.tables[i].guest = None

                free_table_index, cnt_free_tables = self.search_free_table()
                if free_table_index is not None and not self.queue.empty():
                    next_guest = self.queue.get()
                    self.tables[free_table_index].guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел из очереди и сел за стол номер {self.tables[free_table_index].number}")

            if cnt_free_tables == len(self.tables) and self.queue.empty():
                print(f"Свободно столов: {cnt_free_tables}, очереди нет")
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
