import sys


_module_name, sale_num, new_sale = sys.argv
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    for i in range(1, int(sale_num)):
        line = f.readline()
        if not line:
            break
    # итерируем до нужной строки
    if line:
        curs_position = f.seek((f.tell()))
        if f.readline():
            f.seek(curs_position)
            f.write(new_sale)
        else:
            print('Такой строки не существует')
    # тут была проблема если задать номер больше на 1 чем кол-во продаж (в line сохраняется предыдущая строка)
    # поэтому так криво выглядит
    else:
        print('Такой строки не существует')
