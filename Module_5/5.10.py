print('Задача 10. Банкомат')
# Пользователи банкомата хотят снимать деньги.
# Но банкомат умеет выдавать только купюры по 100 рублей.
# Напишите программу,
# которая проверяет допустимость суммы средств, которую ввёл пользователь.

# Пример:
# Введите сумму, которую хотите снять: 250
# Такую сумму снять невозможно. Обратитесь в другой банкомат.

us_money = int(input('How much money do you want to withdraw: '))
if us_money % 100 != 0:
    print('It is not possible to withdraw this amount, Go to another ATM')
else:
    print('Take money please')