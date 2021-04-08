ip_dict = dict()
# Ключи в словаре IP адреса, а значения - кол-во запросов от этого IP
with open('logs_for_parsing.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        ip_num = line.split()[0]
        if ip_num in ip_dict:
            ip_dict[ip_num] += 1
        else:
            ip_dict[ip_num] = 1

print('IP спамера', max(ip_dict, key=lambda k: ip_dict[k]))
# Ищем максимум по значениям в словаре
