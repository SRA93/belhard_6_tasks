"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(dict_one: dict):

    new_dict = {val: key for key, val in dict_one.items()}

    return new_dict


print(reverse_dict({1: 2, 3: 4}))
