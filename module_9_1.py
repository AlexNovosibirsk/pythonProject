
"""
Задача "Вызов разом":
"""


def num_to_str(int_list):
    str_ = str()
    for i in int_list:
        str_ += str(i)
    return str_


def apply_all_func(int_list, *functions):
    results = dict()
    for func in functions:
        try:
            results.update({func.__name__: func(int_list)})
        except TypeError:
            results.update({func.__name__: "TypeError"})
        except ValueError:
            results.update({func.__name__: "ValueError"})
    return results


if __name__ == "__main__":
    print(apply_all_func([4, 1, 2, 3, 0, -5, 6, 7, 8, 0.9], len, sorted, max, min, sum, num_to_str))
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9, " "], len, sum, sorted))
    print(apply_all_func([], len, sorted, max, min, sum, num_to_str))