# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
# Пример:

# 5 -> 1 0 1 1 0
# 2

import numpy as np

def heads_or_tails(size):
    res = 0
    array = np.random.randint(2, size=size)
    nonzero_el = np.count_nonzero(array)
    zero_el = size - nonzero_el
    res = nonzero_el if nonzero_el < zero_el else zero_el
    print (f'Your array: {array}')
    print (res)

heads_or_tails(5)