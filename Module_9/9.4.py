"""

Задача 4. Среднее на отрезке
Что нужно сделать
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит
на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

"""
start = int(input('Enter start number: '))
stop = int(input('Enter stop number: '))
step = int(input('Enter divider: '))
total_sum = 0
count = 0
for num in range((start + step - start % step), stop, step):   # make start value a multiple of the variable step
    total_sum += num
    count += 1
print('Average value is ', total_sum / count)