"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""

i = 2
while i <= 40:  # до какого числа продолжать генерацию

    if i % 2 == 0:
        print(i)
    i += 1
