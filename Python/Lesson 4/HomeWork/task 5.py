"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
"""
lst = [el for el in range(100, 1001) if el % 2 == 0]
print(lst)
from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(reduce(my_func, lst))
