# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только 
# английские, либо только русские буквы.
# Пример:

# Ввод:
# ноутбук
# Вывод:
# 12

def create_dict(key, value, splitter):
    key = key.split(splitter)
    dict = {}
    for i in key:
        dict.setdefault(i, value)
    return dict

def scrabble_game(dict, text):
    sum = 0
    text = text.upper()
    for i in text:
        sum += dict[i]

    return sum

arg = ', '
temp_dict = {
            'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т' : 1,
            'D, G, Д, К, Л, М, П, У' : 2,
            'B, C, M, P, Б, Г, Ё, Ь, Я' : 3,
            'F, H, V, W, Y, Й, Ы' : 4,
            'K, Ж, З, Х, Ц, Ч' : 5,
            'J, X, Ш, Э, Ю' : 8,
            'Q, Z, Ф, Щ, Ъ' : 10
            }

# Create the dictionary
scrabble = {}
for (k,v) in temp_dict.items():
    dict = create_dict(k, v, arg)
    scrabble.update(dict)

# Let play in Scrabble
text = input('Input text: ')
print('Result: {}'.format(scrabble_game(scrabble, text)))
