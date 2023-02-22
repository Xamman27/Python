# Задача 8. Колонтитул
# Что нужно сделать
# Нам нужно написать программу для печати важных объявлений. Вверху объявления должен располагаться такой колонтитул:
# ~~~~~~~~~~!!!~~~~~~~~~~
#
# Восклицательные знаки всегда располагаются по центру строки, причём, в зависимости от важности объявления, количество
# восклицательных знаков может быть разным. Напишите программу, которая спрашивает у пользователя сначала общую длину
# колонтитула в символах, потом желаемое количество восклицательных знаков, после чего выводит на экран готовую строку.

flag = True
while flag:
    length = int(input('Enter the length of the string: '))
    exclam_sym = int(input('Enter the number of exclamation marks: '))
    if (length - exclam_sym) % 2 > 0:
        print('If the string length is even, then the number of exclamation mark must also be even and vice versa')
        print('Repeat input again')
    else:
        flag = False
string = ((length - exclam_sym) // 2) * '~' + exclam_sym * '!' + ((length - exclam_sym) // 2) * '~'
print(string)
