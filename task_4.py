def thesaurus_adv(*names):
    full_name_dict = {}
    for full_name in names:
        first_name_dict = {}
        first_name, last_name = full_name.split()
        if last_name[0] in full_name_dict:
            for first_let_name in full_name_dict[last_name[0]].copy():
                if first_let_name == first_name[0]:
                    full_name_dict[last_name[0]][first_let_name].append(full_name)
                else:
                    full_name_dict[last_name[0]].setdefault(first_name[0], [full_name])
        else:
            list_of_names = [full_name]
            first_name_dict.setdefault(first_name[0], list_of_names)
            full_name_dict.setdefault(last_name[0], first_name_dict)
    return full_name_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))