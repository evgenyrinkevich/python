PHRASE_LIST = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
phrase_correct = []
for element in PHRASE_LIST:
    if element.isdigit():
        element = f'{int(element):02}'
        phrase_correct.extend([f'"{element}"'])
    elif element[0] == '+' or element[0] == '-' and element[1:].isdigit():
        element = element[0] + f'{int(element[1:]):02}'
        phrase_correct.extend([f'"{element}"'])
    else:
        phrase_correct.append(element)
print(' '.join(phrase_correct))
