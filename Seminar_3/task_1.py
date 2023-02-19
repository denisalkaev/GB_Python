# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в 
# массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# Пример:

# 5
# 1 2 3 4 5
# 3
# -> 1

import numpy as np

def search_num(size, search):
    array = np.random.randint(1, size, size=size)
    res = len(np.where(array == search)[0])
    print(*array)
    print(res)

search_num(5, 1)
