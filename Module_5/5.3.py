"""
После выполненной задачи Вася устал и понял, что весь следующий день
ему придётся восстанавливать силы. Вася решил, что работать он будет
только в чётные дни и написал небольшую программу, которая поможет ему
не пропустить рабочий день.
Напишите программу, которая проверяет, чётное ли число ввёл пользователь
и выводит соответствующее сообщение.
Подсказка: для проверки чётности используйте оператор %.
"""
day_month = int(input('Enter the day in the month: '))
if 0 < day_month <= 31:
    if day_month % 2:
        print('Today is not an even day on the moth, Vasya rest!')
    else:
        print("Today is an even day on the month, Vasya go work!")
else:
    print('No such date exists!')
