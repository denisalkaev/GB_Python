# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

import numpy as np

def search_num(size, search):
    array = np.random.randint(1, size, size=size)
    array_ = abs(array - search)
    res = np.argmin(array_)

    print(*array)
    print(array[res])

search_num(10, 9)