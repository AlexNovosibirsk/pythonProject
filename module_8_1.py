"""
Задание "Программистам всё можно":
"""


def add_everything_up(a, b):
    try:
        c = a + b
    except TypeError as exc:
        print(f"TypeError {exc}")
        return str(a) + str(b)
    else:
        return c


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))


