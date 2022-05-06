'''
Задача 7
Найти произведение цифр числа.
    Пример:
    254314
    Произведение цифр числа - 480(2*5*4*3*1*4)
'''

res = 1
while True:
    number = input('Input number: ')
    if number == 'e' or number == 'exit':
        break
    if not number.isnumeric():
        continue
    for i in number:
        res *= int(i)
    print('Произведение цифр числа -', res)
    res = 1