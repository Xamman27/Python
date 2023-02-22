"""
Задача 7. Стипендия

Что нужно сделать
Ежемесячная стипендия студента составляет educational_grant рублей, а расходы на проживание превышают
стипендию и составляют expenses рублей в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
Составьте программу расчёта суммы денег, которую необходимо получить у родителей один раз в начале обучения, чтобы
можно было прожить учебный год (десять месяцев), используя только эти деньги и стипендию.

Пример:
Введите стипендию: 10000
Введите расходы на проживание: 13000
У родителей необходимо попросить 49030.431
"""
total_expenses = 0
educational_grant = int(input('Enter your education grant: '))
expenses = int(input('Enter your living expenses: '))
for month in range(10):
    if month > 0:
        expenses = expenses + (expenses / 100) * 3
        total_expenses += expenses
    else:
        total_expenses += expenses
print('From parent should be asked: ', total_expenses - educational_grant * 10)