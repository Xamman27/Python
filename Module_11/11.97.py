# Задача 7. Наибольшая сумма цифр
# Что нужно сделать
# Пользователь вводит N чисел. Среди натуральных чисел, которые были введены, найдите
# наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input('How much number will be input: '))
max_sum_digit = 0

for i in range(n):
    number = int(input('Enter the number: '))
    div_count = 0
    for y in range(1, number + 1):
        if number % y == 0:
            div_count += 1
            if div_count > 2:
                break
        else:
            sum_digit = 0
            while True:
                if number > 9:
                    sum_digit += number % 10
                    number = number // 10
                else:
                    sum_digit += number
                    if sum_digit > max_sum_digit:
                        max_sum_digit = sum_digit
                    break
print('The maximum sum of digits in natural number is', max_sum_digit)