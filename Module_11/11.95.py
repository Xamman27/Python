# Задача 5. Простые числа
# Что нужно сделать
# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.
# Пример:
# Введите кол-во чисел: 6
# Введите число: 4
# Введите число: 7
# Введите число: 20
# Введите число: 3
# Введите число: 11
# Введите число: 37
# Количество простых чисел в последовательности: 4
# Советы и рекомендации
# Вспомните, что простое число — натуральное (целое положительное) число, имеющее ровно
# два различных натуральных делителя — единицу и самого себя.
count = 0
prime_num_count = 0 # prime number count
count_num = int(input('Enter Quantity numbers: '))
while True:
    num = int(input('Enter the number: '))
    if num > 0:
        count += 1
        div_count = 0 # Divider count, reset with each new input num
        for i in range(1, num + 1):
            if num % i == 0:
                div_count += 1
            if div_count > 2:
                break
        else:
            prime_num_count += 1
        if count == count_num:
            break
print('Number of prime numbers is', prime_num_count)



