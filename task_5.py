import sys


_module_name, users_file, hobbies_file, usr_hobby_file = sys.argv
print(users_file, hobbies_file, usr_hobby_file)
usr_file = open(users_file, 'r', encoding='utf-8')
hobby_file = open(hobbies_file, 'r', encoding='utf-8')
usr_hobbies = open(usr_hobby_file, 'w', encoding='utf-8')
usr_hobby_dict = dict()
for usr_name in usr_file:
    usr_name = usr_name.replace('\n', '').replace('\r', '')
    name_tuple = tuple(usr_name.split(','))
    hobbies = hobby_file.readline().replace('\n', '').replace('\r', '')
    hobbies_tuple = tuple(hobbies.split(','))
# Получаем в name_tuple кортеж( чтобы использовать в качестве ключа словаря) с именем пользователя
# А в hobbies_tuple - кортеж из хобби
    if hobbies:
        usr_hobby_dict[name_tuple] = hobbies_tuple
    else:
        usr_hobby_dict[name_tuple] = None
print(usr_hobby_dict)
usr_hobbies.write(str(usr_hobby_dict))

usr_file.close()
hobby_file.close()
usr_hobbies.close()
