def translate_adv(word):
    dict = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
        'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'One': 'Один', 'Two': 'Два', 'Three': 'Три',
        'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять',
        'Ten': 'Десять'
    }
    if word in dict:
        print(dict.get(word))
    else:
        print('None')


translate_adv(input('Введите слово для перевода: '))