from random import choice


def get_jokes(n, flag=False):
    """Функция генерации шуток"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    """Проверяем заданное число шуток и флаг уникальности"""
    if n > max(map(len, [nouns, adverbs, adjectives])) and flag is True:
        print('Мало уникальных слов в списках для шуток, будет выдано 5(максимальное кол-во) уникальных шуток')
        return get_jokes(5, True)
    """Тело функции, где создаем шутку"""
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke.append(f'{noun} {adverb} {adjective}')
        """и удаляем уже использованные слова из наших списков слов"""
        if flag is True:
            if noun in nouns:
                nouns.remove(noun)
            if adverb in adverbs:
                adverbs.remove(adverb)
            if adjective in adjectives:
                adjectives.remove(adjective)
    return joke


print(get_jokes(6, True))
print(get_jokes(7))
