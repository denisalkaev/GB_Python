# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k),
# не превосходящие числа N.
# Пример:

# 10 -> 1 2 4 8

def int_num(value):
    array = [2**i for i in range(value) if 2**i < value]
    print(*array)

num = int(input('Input the number: '))
int_num(num)