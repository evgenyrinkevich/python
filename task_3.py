def thesaurus(*args):
    names_dict = {}
    for name in args:
        if name[0] in names_dict:
            names_dict.get(name[0]).append(name)
        else:
            _names_list = [name]
            names_dict.setdefault(name[0], _names_list)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Имя", "Пупя"))