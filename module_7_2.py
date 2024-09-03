"""
Задача "Записать и запомнить"
"""
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding="utf-8")
    for i in range(len(strings)):
        strings_positions[i + 1, file.tell()] = strings[i]
        file.write(strings[i] + "\n")
    file.close()
    return strings_positions


if __name__ == "__main__":
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
