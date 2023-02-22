# Задача 3. Лестница чисел
#
# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

n = int(input('Enter the number: '))
for col in range(n):
    for row in range(col, n):
        print(row, end='\t')
    print()