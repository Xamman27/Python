# Задача 2. Лестница
# Что нужно сделать
#
# Пользователь вводит число N. Напишите программу, которая выводит такую «лесенку» из чисел:

n = int(input('Enter the number: '))
for col in range(1, n + 1):
    for row in range(col):
        print(col, end=' ')
    print()