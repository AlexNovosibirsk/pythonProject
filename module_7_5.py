import os
import time


if __name__ == "__main__":
    # Небольшой эксперимент по созданию нового каталога
    try:
        os.mkdir("Second")
    except FileExistsError:
        print(f" Файл уже существует в {os.getcwd()}")

    #  file_name = "Mother Goose - Monday’s Child.txt"
    file_name = "module_7_5.py"
    directory = "."
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:

                filepath = os.path.join(root, file)
                filesize = os.path.getsize(file)
                filetime = os.path.getmtime(file)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
                parent_dir = os.path.dirname(filepath)

                print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, ')
                print(f'Время изменения: {formatted_time}, ')
                print(f'Родительская директория: {parent_dir}')


# Обнаружен файл: Mother Goose - Monday’s Child.txt, Путь: .\Mother Goose - Monday’s Child.txt, Размер: 347 байт,
# Время изменения: 30.06.2024 05:28,
# Родительская директория: .

# Обнаружен файл: module_7_5.py, Путь: .\module_7_5.py, Размер: 1371 байт,
# Время изменения: 09.09.2024 21:35,
# Родительская директория: .

