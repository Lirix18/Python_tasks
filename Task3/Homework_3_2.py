dictionary = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }


def translate_adv(word):
    for eng, rus in dictionary.items():
        if eng == word:
            return rus
        elif eng.title() == word:
            return rus.title()


print(translate_adv('Seven'))
print(translate_adv('one'))
print(translate_adv('10'))
