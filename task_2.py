eng_rus_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate(eng_num):
    if eng_num[0].isupper() and eng_num.lower() in eng_rus_dict:
        rus_num = eng_rus_dict.get(eng_num.lower()).title()
    else:
        rus_num = eng_rus_dict.get(eng_num)
    return rus_num


print(num_translate('zero'))