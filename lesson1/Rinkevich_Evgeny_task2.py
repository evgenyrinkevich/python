qubes = []
sum_final = 0
sum_final_plus17 = 0
for i in range(1, 1001, 2):
    qubes.append(i**3)
    current_number = qubes[-1]
    current_number_plus17 = qubes[-1] + 17
    sum_of_digits = 0
    while current_number > 0:
        digit = current_number % 10
        sum_of_digits += digit
        current_number = current_number // 10

    if sum_of_digits % 7 == 0:
        sum_final += qubes[-1]
        # print(qubes[-1], '1 array')    для проверки правильности подсчета вывожу подходящие числа

    sum_of_digits = 0
    while current_number_plus17 > 0:
        digit = current_number_plus17 % 10
        sum_of_digits += digit
        current_number_plus17 = current_number_plus17 // 10

    if sum_of_digits % 7 == 0:
        sum_final_plus17 += qubes[-1] + 17
        # print(qubes[-1], '2 array')   для проверки правильности подсчета вывожу подходящие числа 2го задания

print(f'1ая сумма: {sum_final}, 2ая сумма: {sum_final_plus17}')
