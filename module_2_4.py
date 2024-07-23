"""
Задача "Всё не так уж просто":
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Используя этот список составьте второй список primes содержащий только простые числа.
А так же третий список not_primes, содержащий все не простые числа.
Выведите списки primes и not_primes на экран(в консоль).
"""

primes = []
not_primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


for i in range(len(numbers)):

    if numbers[i] == 1:
        continue
    is_prime = False

    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = True
            break

    if is_prime:
        not_primes.append(numbers[i])
    else:
        primes.append(numbers[i])

print("Not Primes:", not_primes)
print("Primes:", primes)

# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
# Primes: [2, 3, 5, 7, 11, 13]
