"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""


def common_numbers(lst_one: list, lst_two: list):

    lst_all = list(set(lst_one).intersection(set(lst_two)))
    lst_all.sort(reverse=True)
    return lst_all


lst_one = [1, 3, 8, 4, 5]
lst_two = [4, 5, 6, 7, 8]


print(common_numbers(lst_one, lst_two))
