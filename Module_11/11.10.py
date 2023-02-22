# Задача 2. Цифры больше пяти
#
# Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее
# количество цифр больше пяти во всей последовательности.
#
count_more_5 = 0
n = int(input('How many numbers will be? :'))
for num in range(n):
    number = int(input('Enter the number: '))
    for sym in str(number):
        if int(sym) > 5:
            count_more_5 += 1
print('The total number of digit greatest 5 is', count_more_5)



