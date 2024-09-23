"""
Задание: Декораторы в Python
"""


def is_prime(func):
    def wrapper(*args):
        res = func(*args)

        isPrime = False
        for i in range(2, res):
            if res % i == 0:
                isPrime = True
                break
        if isPrime:
            print("Составное")
        else:
            print("Простое")
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


print(sum_three(2, 3, 6))
print(sum_three(2, 3, 6, 1,5,9,23))



