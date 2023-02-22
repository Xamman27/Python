
num = int(input('Enter the number: '))
summ_value = 0
for n in range(num + 1):
    value = (-1) ** n * (1 / 2 ** n)
    summ_value += value
print(summ_value)