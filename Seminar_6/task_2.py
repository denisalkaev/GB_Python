# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def my_filter(min, max, array):
    array = list(filter(lambda x: min < x <= max, array))
    return sorted(array)

array = [random.randint(0, 100) for i in range(10)]
print(array)
res = my_filter(10, 50, array)
print(res)