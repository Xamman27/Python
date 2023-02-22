# Задача 3. Рамка
# Что нужно сделать
# Напишите программу, которая рисует с помощью символьной графики прямоугольную рамку. Для вертикальных линий
# используйте символ вертикального штриха (|), а для горизонтальных — дефис (-). Пусть
# пользователь вводит ширину и высоту рамки.

width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
for col in range(height):
    for row in range(width):
        if col == 0 or col == height - 1:
            print('-', end=' ')
        elif row == 0 or row == width - 1:
            print('|', end=' ')
        else:
            print(' ', end=' ')
    print()