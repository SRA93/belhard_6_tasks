"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    n = 1
    while True:
        res = 1
        for i in range(1, n + 1):
            res *= i
        yield res
        n += 1


factorial_next = factorial()

print(next(factorial_next))
print(next(factorial_next))
print(next(factorial_next))
print(next(factorial_next))
