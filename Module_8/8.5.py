"""
Задача 5. Отрезок
Что нужно сделать
Напишите программу, которая считывает с клавиатуры два числа: a и b, — считает и выводит в
консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу 3.
"""
start_num = int(input('Enter a number for the beginning of the segment: '))
stop_num = int(input('Enter a number of the end of the segment '))
total_sum = 0
count_num = 0
if start_num < stop_num:
    for num in range(start_num, stop_num + 1):
        if num % 3 == 0:
            total_sum += num
            count_num += 1
else:
    print('the first number must be less than the second')
print('Average value in the range from', start_num, 'to', stop_num, 'multiples of 3 is', total_sum / count_num)
