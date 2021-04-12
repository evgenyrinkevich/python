import os
# Предположил что кратный 2ум отступ определяет структуру стартера
# Элементы разделены ':'


def create_file_or_dir(name):
    """
    Создает файл или папку в зависимости от имени
    (предполагаю, что name без . это папка)
    """
    if '.' in name:
        open(name, 'w').close()
    else:
        os.makedirs(name, exist_ok=True)


with open('config.yaml', 'r', encoding='utf-8') as config:
    conf_text = config.read().replace(':', '').strip()
    paragraphs = conf_text.splitlines()
    os.makedirs(paragraphs[1], exist_ok=True)
    os.chdir(paragraphs[1])
    # файл разбили на список из строк paragraphs, 2ая строка это имя родит. папки
    curr_indent = 2
    for line_num in range(2, len(paragraphs)):
        if paragraphs[line_num].count(' ') == curr_indent:
            create_file_or_dir(paragraphs[line_num].strip())
            # если отступ не изменился создаем папку/файл
        elif paragraphs[line_num].count(' ') > curr_indent:
            os.chdir(os.path.join('./', paragraphs[line_num - 1].strip()))
            # если отступ увеличился переходим в папку из пред строки
            create_file_or_dir(paragraphs[line_num].strip())
            curr_indent = paragraphs[line_num].count(' ')
        else:
            for i in range(int(curr_indent / paragraphs[line_num].count(' ')) - 1):
                os.chdir('..')
            # елси отступ уменьшился переходим вверх
            # в зависимости от того на насколько уменьшился
            create_file_or_dir(paragraphs[line_num].strip())
            curr_indent = paragraphs[line_num].count(' ')
