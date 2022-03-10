dictionary = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }


def translate(word):
    if word in dictionary:
        return dictionary.get(word)


print(translate('7'))
print(translate('one'))
