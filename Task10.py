'''
Задача 10
Найти количество цифр 5 в числе
    Пример:
        543231235643
        'В числе 2 5-ки.'
'''
while True:
    number = input('Input number: ')
    if number == 'e' or number=='exit':
        break
    countFive = number.count('5')
    print('Количество цифр 5:',countFive )
