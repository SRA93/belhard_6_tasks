"""
Написать рекурсивную функцию factorial, которая будет возвращать n-ый элемент
"""
def factorial(n: int, curent=1, result: int = 1 ):
    if current <= n:
        factorial(n, curent + 1, result * current)
    else:
        return result


    print(factorial(3))