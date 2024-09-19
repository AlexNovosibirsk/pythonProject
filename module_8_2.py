"""
Задача "План перехват"
"""


def personal_sum(numbers):
    result_summ, incorrect_data = 0, 0

    for element in numbers:
        try:
            result_summ += element
        except TypeError:
            print("Некорректный тип данных для подсчёта суммы - ", element)
            incorrect_data += 1

    return result_summ, incorrect_data


def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
        return summ / len(numbers), incorrect_data
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
    print(f'Результат 5: {calculate_average([])}')
    print(f'Результат 6: {calculate_average(5.67)}')
