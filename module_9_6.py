"""
Задача "Генераторы"
"""


def all_variants(text):
    for _ in range(len(text)):
        yield text[_]
    for _ in range(len(text)-1):
        yield text[_] + text[_+1]
    yield text


if __name__ == "__main__":
    f = all_variants("abc")
    for i in f:
        print(i)
    f = all_variants("abcd")
    for i in f:
        print(i)
