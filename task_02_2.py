# 39. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 221 конфета.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# В качестве дополнительного усложнения можно:
# a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

import random
print()
print('"Игра с конфетами"')
print('Условия игры следующие:\n\
1) На столе лежит 221 конфета. Вы играете против компьютера. Ходите поочередно.\n\
2) Первый ход определяется жеребьёвкой.\n\
3) За один ход можно забрать не более чем 28 конфет, но не меньше 1.\n\
4) Все конфеты оппонента достаются сделавшему последний ход."')

start=input('Если условия понятны, то для начала игры, напишите команду: /start\n:')
while start!='/start':
    start=input('Для начала игры, напишите команду: /start\n:')

print('Начнём игру!')
player_number = random.randint(1, 2)
if player_number == 1:
    print('Первым ходит компьютер.')
else:
    print('Первым ходите Вы.')

start = 221
count = 0

while start > 28:
    count += 1
    print(f'{count} ход. На столе сейчас лежит {start} конфет(а).')

    if player_number == 1:
        candies = random.randint(1, 28)
        start -= candies
        print(f'Компьютер взял {candies} конфет(ы).')
        player_number=2

    else:
        user_input = input('Сколько конфет Вы возьмете со стола: ')
        while not user_input.isdigit():
            print(f'{user_input} - не число! Попробуйте снова.')
            user_input = input('Сколько конфет Вы возьмете со стола: ')
        while int(user_input) < 1 or int(user_input) > 28:
            print(f'Вы должны взять хотя бы 1 конфету, но не больше 28. Попробуйте снова.')
            user_input = input('Сколько конфет Вы возьмете со стола: ')
            while not user_input.isdigit():
                print(f'{user_input} - не число! Попробуйте снова.')
                user_input = input('Сколько конфет Вы возьмете со стола: ')
        user_input = int(user_input)
        start -= user_input
        player_number=1

while start > 0:
    count += 1
    print(f'{count} ход. На столе сейчас лежит {start} конфет(а).')

    if player_number == 1:
        candies = random.randint(1, start)
        start -= candies
        print(f'Компьютер взял {candies} конфет(ы).')
        player_number=2

    else:
        user_input = input('Сколько конфет Вы возьмете со стола: ')
        while not user_input.isdigit():
            print(f'{user_input} - не число! Попробуйте снова.')
            user_input = input('Сколько конфет Вы возьмете со стола: ')
        while int(user_input) < 1 or int(user_input) > start:
            print(f'Вы должны взять хотя бы 1 конфету, но не больше {start}. Попробуйте снова.')
            user_input = input('Сколько конфет Вы возьмете со стола: ')
            while not user_input.isdigit():
                print(f'{user_input} - не число! Попробуйте снова.')
                user_input = input('Сколько конфет Вы возьмете со стола: ')
        user_input = int(user_input)
        start -= user_input
        player_number=1

if player_number == 1:
    print('Поздравляю! Вы победили!')
else:
    print('Увы, в этот раз не повезло. Победил компьютер. Попробуйте сыграть снова!')
