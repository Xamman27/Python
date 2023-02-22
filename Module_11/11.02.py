# Задача 2. Таблица суммы
# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.

num = int(input('Enter the number: '))
for x in range(0, num + 1):
    for y in range(0, num + 1):
        print(x + y, end='\t')
    print()