"""
Задача "Банковские операции"
"""

from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock_print = Lock()

    def deposit(self):
        for i in range(100):
            rand = randint(50, 500)
            self.balance += rand
            self.printf("\033[92m"+f"Пополнение: {rand}. Баланс: {self.balance}"+"\033[0m")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.01)

    def take(self):
        for i in range(100):
            rand = randint(50, 500)
            self.printf(f"Запрос на {rand}")
            if rand <= self.balance:
                self.printf(f"Снятие: {rand}. Баланс: {self.balance}")
                self.balance -= rand
            else:
                self.printf(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.01)

    def printf(self, strf):
        with self.lock_print:
            print(strf)


if __name__ == "__main__":
    bk = Bank()
    
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
