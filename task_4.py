import os
from os.path import join
import json


def add_to_dict(min_size, max_size):
    # если файл нужного размера увеличиваем счетчик на 1
    # если в словаре нет такого разрешения - добавляем разрешение
    if min_size < os.stat(join(root, name)).st_size <= max_size:
        result_dict[max_size][0] += 1
        ext = os.path.splitext(join(root, name))[1]
        if ext not in result_dict[max_size][1]:
            result_dict[max_size][1].append(ext)


FOLDER_PATH = './some_data'
result_dict = {
    100: [0, []],
    1000: [0, []],
    10000: [0, []],
    100000: [0, []]
}

for root, dirs, files in os.walk(FOLDER_PATH):
    for name in files:
        add_to_dict(0, 100)
        add_to_dict(100, 1000)
        add_to_dict(1000, 10000)
        add_to_dict(10000, 100000)

for size in result_dict:
    result_dict[size] = tuple(result_dict[size])

print(result_dict)
with open(f'{FOLDER_PATH}_summary.json', 'w') as f:
    json.dump(result_dict, f, indent=2)
