"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""


def to_set(some_list):

    new_set = set(some_list)
    print(len(new_set))
    return new_set
