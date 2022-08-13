def translate(word):
    dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if word in dict:
        print(dict.get(word))
    else:
        print('None')


translate(input('Введите слово для перевода: '))