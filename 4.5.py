minute = int(input('Enter a number greater than 60: '))
hour = minute // 60
rem_m = hour % 60
print(hour, 'hour', rem_m, 'minute')