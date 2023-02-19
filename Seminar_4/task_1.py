# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
# наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
#  второго множества. Затем пользователь вводит сами элементы множеств.

import numpy as np

def get_array(n, m, max_value):
    array_1 = np.random.randint(max_value, size=n)
    array_2 = np.random.randint(max_value, size=m)
    print('First array:', *array_1)
    print('Second array:', *array_2)
    res = sorted(set(array_1).intersection(set(array_2)))
    print('Resulted array:', *res)

get_array(15, 20, 100)