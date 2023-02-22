"""
Напишите программу, которая выводит на экран максимальное из
этих трёх чисел (все числа разные). Используйте дополнительные
переменные, если нужно.
"""
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
num_3 = int(input('Enter the third number: '))
if num_2 <= num_1 >= num_3:
    win_num = num_1
elif num_1 <= num_2 >= num_3:
    win_num = num_2
else:
    win_num = num_3
print('Largest number', win_num )