# Написать скрипт, который собирает все шаблоны в одну папку templates.
# Под словом "шаблон" скорее всего имеются ввиду файлы .html - это ответ наставника
# Тут переписал все html файлы в стартере project в новую папку /templates/относит путь .html файла
import os
from os.path import relpath


root_dir = '/Users/Stas/Desktop/Tutorials/Python Projects/pythonProject/project'
os.chdir(root_dir)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        if ext == 'html':
            rel_path = relpath(root, root_dir)
            dest_path = os.path.join('templates', rel_path)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            open(os.path.join(dest_path, file), 'w').close()
