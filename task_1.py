import requests


logs = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('logs_for_parsing.txt', 'w', encoding='utf-8') as f:
    f.write(logs.text)

parsed_list = []
with open('logs_for_parsing.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line_list = line.split()
        # Разбил каждую строку и нашел нужные элементы
        result_tuple = (line_list[0], line_list[5].strip('"'), line_list[6])
        parsed_list.append(result_tuple)
print(parsed_list)
