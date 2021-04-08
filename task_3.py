with open('users.csv', 'r', encoding='utf-8') as f:
    users = f.read()
    users_list = users.splitlines()

with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby = f.read()
    hobby_list = hobby.splitlines()

usr_hobby_dict = dict()
if len(users_list) > len(hobby_list):
    for i in range(len(hobby_list)):
        usr_hobby_dict[users_list[i]] = hobby_list[i]
    for i in range(len(hobby_list), len(users_list)):
        usr_hobby_dict[users_list[i]] = None
else:
    for i in range(len(hobby_list)):
        usr_hobby_dict[users_list[i]] = hobby_list[i]
# Если список пользователей длиннее списка хобби - в остаток записываем Имя: None
# Если короче - вылетаем с ошибкой
print(usr_hobby_dict)
with open('usr_hobby.txt', 'w', encoding='utf-8') as f:
    f.write(str(usr_hobby_dict))
