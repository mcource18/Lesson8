'''
Задача 9
Найти максимальную цифру в числе
Пример:
    354359688
    'Цифра - 9 максимальная в числе 354359688'
'''

sum = 0
while True:
    number = input('Input number: ')
    if number == 'e' or number=='exit':
        break
    if not number.isnumeric():
        continue
    for i in number:
        digit = int(i)
        if sum < digit:
            sum = digit
    print(sum)
    sum = 0
