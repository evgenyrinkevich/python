weather_report = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(weather_report)):
    if weather_report[i].isdigit():
        weather_report[i] = f'"{int(weather_report[i]):02}"'
    elif weather_report[i][0] == '+' or weather_report[i][0] == '-' and weather_report[i][1:].isdigit():
        weather_report[i] = f'"{weather_report[i][0]}{int(weather_report[i][1:]):02}"'

print(' '.join(weather_report))
