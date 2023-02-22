# Задача 9. Пирамидка 2
# Что нужно сделать
#
# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран,
# заполняя нечётными числами, вот так:


num = 1
height = int(input('Enter the height: '))
for col in range(height):
    print((height - col - 1) * '    ', end='')
    for row in range(col + 1):
        print(num, end='    ')
        num += 2
    print()