"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(list_one: list):

    gen_list = []

    for i in list_one:

        if i not in gen_list:
            print('No')
            gen_list.append(i)

        else:
            print('Yes')


yes_or_no([2, 3, 6, 3, 33, 5, 2])
