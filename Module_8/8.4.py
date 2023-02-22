"""
Задача 4. Успеваемость в классе
Что нужно сделать
В классе N человек. Каждый из них получил за урок по информатике оценку: 3, 4 или 5,
двоек сегодня не было. Напишите программу, которая получает список оценок — N чисел — и
выводит на экран сообщение о том, кого сегодня больше: отличников, хорошистов или троечников.

Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.
"""
count_3 = 0
count_4 = 0
count_5 = 0
total_students = int(input('Numbers of students in the class: '))
for student in range(total_students):
    rating = int(input('Enter rating: '))
    if rating == 3:
        count_3 += 1
    elif rating == 4:
        count_4 += 1
    else:
        count_5 += 1

if count_3 < count_5 > count_4:
    most_st = 5
elif count_5 < count_3 > count_4:
    most_st = 3
else:
    most_st = 4
print('Most student got grade of', most_st)