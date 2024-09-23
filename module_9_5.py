"""
Задача "Range - это просто":

__init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
В этом методе в первую очередь проверяется step на равенство 0.
Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
__iter__ - метод сбрасывающий значение pointer на start и возвращающий сам объект итератора.
__next__ - метод увеличивающий атрибут pointer на step.
В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop,
либо меньше stop. Учтите это при описании метода.
"""


class StepValueError(ValueError):
    pass


class Iterator:
    def __new__(cls, start: int, stop: int, step=1, **kwargs):
        instance = super().__new__(cls)
        if step == 0:
            raise StepValueError
        return instance

    def __init__(self, start: int, stop: int, step=1):
        self.start = start    # целое число с которого начинается итерация.
        self.stop = stop      # целое число на котором заканчивается итерация.
        self.step = step      # шаг с которой совершается итерация.
        self.pointer = start  # указывает на текущее число в итерации (изначально start)

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step

        if self.pointer < self.stop and self.step < 0:
            raise StopIteration()

        if self.pointer > self.stop and self.step > 0:
            raise StopIteration()

        return self.pointer


if __name__ == "__main__":
    try:
        iter1 = Iterator(100, 200, 0)
        for i in iter1:
            print(i, end=' ')
    except StepValueError:
        print('Шаг указан неверно')

    iter2 = Iterator(-5, 1)
    iter3 = Iterator(6, 15, 2)
    iter4 = Iterator(5, 1, -1)
    iter5 = Iterator(10, 1)

    for i in iter2:
        print(i, end=' ')
    print()
    for i in iter3:
        print(i, end=' ')
    print()
    for i in iter4:
        print(i, end=' ')
    print()
    for i in iter5:
        print(i, end=' ')
    print()
