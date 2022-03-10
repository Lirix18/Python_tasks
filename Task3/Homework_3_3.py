my_list = "Иван", "Мария", "Петр", "Илья"


def thesaurus(*input_list):
    dictionary = {}
    for i in input_list:
        name = []
        name += [n for n in input_list if n.startswith(list(i)[0])]
        dictionary[list(i)[0]] = name
    return dictionary


print(thesaurus(*my_list))


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
