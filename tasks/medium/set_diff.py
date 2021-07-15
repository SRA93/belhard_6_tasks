"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(set_one: set, set_two: set, set_three: set, symmetric=False):

    if symmetric is False:
        return set_one.difference(set_two, set_three)

    elif symmetric is True:
        return set_one.symmetric_difference(set_two, set_three)
