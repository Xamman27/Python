# Задача 6. Сумма факториалов
# Что нужно сделать
#
# Напишите программу, которая запрашивает у пользователя число N и находит сумму факториалов 1! + 2! + 3! + ... + n!
#
sum_factorial = 0
n = int(input('Enter the number: '))
for num in range(1, n + 1):
    num_factorial = 1
    for factor in range(1, num + 1):
        num_factorial *= factor
    sum_factorial += num_factorial
    print(num, '!=', num_factorial)
print('Sum of factorials', sum_factorial)