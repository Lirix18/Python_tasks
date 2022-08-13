my_list = ("Иван", "Мария", "Петр", "Илья")
dict = {}


def thesaurus(input_list):
    for i in input_list:
        letter = list(i)[0]
        name = []
        name += [n for n in input_list if n.startswith(letter)]
        dict[letter] = name
    print(dict)


thesaurus(my_list)
