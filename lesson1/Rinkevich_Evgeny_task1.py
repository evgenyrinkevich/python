duration = int(input('Введите время в сек: '))
days = duration // 86400
hours = (duration % 86400) // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60
if duration < 60:
    print(seconds, 'секунд(a)')
elif duration < 3600:
    print(minutes, 'минут(a)', seconds, 'секунд(a)')
elif duration < 86400:
    print(hours, 'часов(a)', minutes, 'минут(a)', seconds, 'секунд(a)')
else:
    print(days, 'дня(ей)', hours, 'часов(a)', minutes, 'минут(a)', seconds, 'секунд(a)')