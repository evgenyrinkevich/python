import sys

try:
    _module_name, sale = sys.argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{sale}\n')
except ValueError:
    print('Введите сумму продаж')
