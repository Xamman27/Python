num = int(input('Enter four-digit number: '))
print('number consist of :', num // 1000, '   ',
    (num // 100) % 10, '   ',
    num % 100 // 10, '   ',
    num % 1000 % 100 % 10)