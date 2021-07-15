"""
Написать рекурсивную функцию  line_print, которая принимает 1 аргумент - список

Функция печатает каждых элемент на новой строке.

Если элемент списка - список, то его элементы должны выводиться с отступом
относительно родительского на одну табуляцию

Например:

some_list = [1, 2, [1, 2, [5, 7], 3], 8]

line_print(some_list)
1
2
    1
    2
        5
        7
    3
8
"""


def line_print(some_list: list, new_str=0):

    for x in some_list:
        if isinstance(x, list):
            line_print(x, new_str + 1)
        else:
            print('    ' * new_str + str(x))


some_list = [1, 2, [1, 2, [5, 7], 3], 8]
line_print(some_list)
