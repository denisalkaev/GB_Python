# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить
# k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:

# 3 2 4 -> yes
# 3 2 1 -> no

def ChocolateDiv(x, y, z):
    if z < x * y:
        if z % x == 0 or z % y == 0:
            print('yes')
        else:
            print('no')

x = int(input('Input choco height: '))
y = int(input('Input choco width: '))
z = int(input('Input choco slice: '))

ChocolateDiv(x, y, z)