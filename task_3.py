from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) < len(klasses):  # кол-во кортежей не должно быть больше длины списка tutors
    klasses = [x for x in klasses[:len(tutors)]]

tut_klass = zip_longest(tutors, klasses, fillvalue=None)

next_el_exists = True
while next_el_exists: #Проверяем его работу вплоть до истощения.
    try:
        print(next(tut_klass))
    except StopIteration:
        next_el_exists = False
        print('Генератор истощен')

