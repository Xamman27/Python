# Задача 8. Пирамидка
# Что нужно сделать
#
# Напишите программу, которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега «#». Пусть высота пирамиды вводится пользователем.

height = int(input('Triangle height: '))
width = 2 * height - 1
for col in range(height + 1):
    for row in range(width):
        if col > -row + (height - 1) and col + (height - 1) > row:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()