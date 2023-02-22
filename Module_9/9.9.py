x = int(input('Enter the number: '))
res = 1
temp = 1
for n in range(6):
    temp *= 2
    res *= x - (temp - 1) / x - temp
print(res)