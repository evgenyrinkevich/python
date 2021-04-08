import sys


if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
        print()
elif len(sys.argv) == 2:
    _module_name, sale_num = sys.argv
    sale_count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            sale_count +=1
            cur_sale = line
            if int(sale_num) <= sale_count:
                print(cur_sale, end='')
        print()
elif len(sys.argv) == 3:
    _module_name, sale_start, sale_stop = sys.argv
    sale_count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            sale_count += 1
            cur_sale = line
            if int(sale_start) <= sale_count <= int(sale_stop):
                print(cur_sale, end='')
