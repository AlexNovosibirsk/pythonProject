"""
Задача "Потоковая запись в файлы"
"""

from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count: int, f_name: str):

    with open(f_name, mode="w", encoding="utf-8") as file:
        for i in range(word_count):
            file.write(f'{f_name} № {i}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {f_name}")


if __name__ == "__main__":

    start = datetime.now()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end = datetime.now()
    print(end - start)

    start = datetime.now()
    th_1 = Thread(target=write_words, args=(10, "example5.txt"))
    th_2 = Thread(target=write_words, args=(30, "example6.txt"))
    th_3 = Thread(target=write_words, args=(200, "example7.txt"))
    th_4 = Thread(target=write_words, args=(100, "example8.txt"))
    th_1.start()
    th_2.start()
    th_3.start()
    th_4.start()
    th_1.join()
    th_2.join()
    th_3.join()
    th_4.join()
    end = datetime.now()
    print(end - start)
