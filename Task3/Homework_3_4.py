my_list = "Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"


def thesaurus_adv(*input_list):
    dictionary = {}
    for i in input_list:
        name, surname = i.split()
        if not dictionary.get(surname[0]):  # если нет словаря по букве фамилии
            dictionary[surname[0]] = {name[0]: [i]}
        elif not dictionary[surname[0]].get(name[0]):  # если нет буквы фамилии и буквы имени
            (dictionary[surname[0]])[name[0]] = [i]
        else:
            (dictionary[surname[0]])[name[0]].append(i)  # в остальных случаях добавляем во вложенный словарь
    return dictionary


print(thesaurus_adv(*my_list))


