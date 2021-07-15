"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers():
    numer = 1
    while True:
        yield int(1 / 2 * numer * (numer + 1))
        numer += 1


tn_gen = triangular_numbers()

print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
