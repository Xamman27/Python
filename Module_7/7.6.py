"""
Задача 6. Вклады
Что нужно сделать
Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек
отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей.

Напишите программу, которая по данным числам X, Y, P
определяет, сколько лет пройдёт, прежде чем сумма достигнет значения Y.
"""
deposit = int(input('Enter deposit amount: '))
rate = int(input('Interest rate deposit: '))
result_deposit = int(input('How much money do you want to receive: '))
year = 0
while deposit < result_deposit:
    deposit = (deposit * rate / 10) // 1
    year += 1
print(year, 'years is passed, your deposit is ', deposit)