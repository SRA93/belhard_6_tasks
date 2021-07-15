"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_one: list):

    if len(list_one) > len(set(list_one)):
        print('Yes')

    else:
        print('No')


yes_or_no([2, 3, 6, 7, 33, 5, 2])
