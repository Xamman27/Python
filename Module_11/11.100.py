# Вы пишите компьютерную игру с текстовой графикой, вам поручили написать генератор ландшафта.
# Напишите программу, которая получает на вход число N и выводит на экран числа в виде «ямы», вот так:

height = int(input('Enter the number: '))

for col in range(height, 0, -1):
    for row in range(height * 2, 1, -1):
        if col < row - height + 1 or -col + height + 3 > row:
            print(col, end='')
        else:
            print('.', end='')
    print()