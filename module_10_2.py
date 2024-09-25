"""
Задача "За честь и отвагу!"
"""
from threading import Thread, Lock
from time import sleep

lock = Lock()


class Knight(Thread):

    def __init__(self, name: str, power: int, color: str):
        super().__init__()
        self.name = name  # имя рыцаря. (str)
        self.power = power  # сила рыцаря. (int)
        self.color = color
        self.ammount_enemies = 100

    def run(self):
        cnt_days = 0
        print("\033[91m" + f"{self.name}, на нас напали!" + "\033[0m")

        while self.ammount_enemies:
            cnt_days += 1
            self.ammount_enemies -= self.power
            if self.ammount_enemies < 0:
                self.ammount_enemies = 0

            with lock:  # для корректного вывода применим мьютекс
                print(self.color + f"{self.name}, сражается {cnt_days} день(дня)..., "
                                   f"осталось {self.ammount_enemies} воинов" + "\033[0m")
            sleep(0.45)

        with lock:
            print("\033[92m" + f"{self.name} одержал победу спустя "
                               f"{cnt_days} дней(дня)!" + "\033[0m")


first_knight = Knight('Sir Lancelot', 7, '\033[94m')
second_knight = Knight("Sir Galahad", 12, '\033[93m')

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
