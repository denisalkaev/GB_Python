# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:

# 2 2
# 4

def sum_num(a, b):
    if b == 0:
        return a
    res = sum_num(a + 1, b - 1)

    return res

print(sum_num(125, 125))