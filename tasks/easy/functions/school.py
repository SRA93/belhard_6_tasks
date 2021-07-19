"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""


def incr_students(school_data: dict, sch_class: str):
    return school_data.update({sch_class: school_data.get(sch_class) + 1})


def dect_students(school_data: dict, sch_class: str):
    return school_data.update({sch_class: school_data.get(sch_class) - 1})


def add_class(school_data: dict):
    return school_data.update({school_data: 0})


def remove_class(school_data: dict, sch_class: str):
    school_data.pop(sch_class)
    return school_data


def calc_students(school_data: dict) -> int:
    return sum(school_data.values())


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
