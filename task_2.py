import re
import requests
import os


logs = requests.get(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('logs.txt', 'w', encoding='utf-8') as f:
    f.write(logs.text)


pattern = re.compile(r'(.{8,15}) - - \[(.+)] \"([A-Z]+) /(.+) HTTP.+\" ([0-9]+) ([0-9]+)')

with open('logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        result = pattern.search(line)
        parsed_raw = (result.group(i) for i in range(1, 7))
        print(*parsed_raw, sep=', ')

os.remove("logs.txt")
