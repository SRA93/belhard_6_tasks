"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""


SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(dict_one: dict):

    number = 1

    for i in dict_one.values():
        number *= i
    return number


print(multiply_dict_values(SOME_DICT))
