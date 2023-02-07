# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def SumNumber(value):
    res = 0
    while value !=0:
        res += value % 10
        value //= 10
    return res

num = int(input('Input the number: '))
print(f'The sum of numbers: {SumNumber(num)}')