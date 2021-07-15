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


def incr_students(SCHOOL_DATA: dict, sch_class: str) -> dict:
    return SCHOOL_DATA.update({sch_class: SCHOOL_DATA.get(sch_class) + 1})


def dect_students(SCHOOL_DATA: dict, sch_class: str) -> dict:
    return SCHOOL_DATA.update({sch_class: SCHOOL_DATA.get(sch_class) - 1})


def add_class(SCHOOL_DATA: dict, sch_class: str) -> dict:
    return SCHOOL_DATA.update({SCHOOL_DATA: 0})


def remove_class(SCHOOL_DATA: dict, sch_class: str) -> dict:
    SCHOOL_DATA.pop(sch_class)
    return SCHOOL_DATA


def calc_students(school_data_1: dict) -> int:
    return sum(school_data_1.values())


school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
