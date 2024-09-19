"""
Задача "Некорректность"
"""


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model        # название автомобиля (строка)
        self.__vin = vin          # vin-номер автомобиля (целое число)
        self.__numbers = numbers  # номера автомобиля (строка)
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(self.__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')


# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера










