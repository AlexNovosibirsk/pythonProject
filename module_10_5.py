"""
Задача "Многопроцессное считывание"
"""
import os
import multiprocessing
from datetime import datetime

fileNames = [f'file {number}.txt' for number in range(1, 5)]

def read_info(name):
    all_data = list()
    print(name)
    with open(name, "r") as file:
        for line in file:
            line = line.rstrip('\n')
            all_data.append(line)
    return name


if __name__ == '__main__':

# Линейный вызов
    start = datetime.now()
    print(list(map(read_info, fileNames)))
    end = datetime.now()
    print(end - start)  # 0:00:15.142054

# Многопроцессный
    start = datetime.now()
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        pool.map(read_info, fileNames)
    end = datetime.now()
    print(end - start)  # 0:00:10.845481

