"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(n):
    res = 1

    for i in range(1, n + 1):
        res *= i
    return res


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
