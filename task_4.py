people = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(people)):
    people[i] = people[i].split()[-1]
    print(f'Привет {people[i].capitalize()}')

