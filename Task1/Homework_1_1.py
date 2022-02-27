duration = input('Введите продолжительность в секундах: ')
min = 60
hour = min * 60  # 3600 секунд
day = hour * 24  # 86400 секунд
year = day * 365  # 31536000 секунд не високосный год
try:
    list_dur = list(map(int, duration.split()))  # создание списка из введенных значений в формате int
    for duration in list_dur:
        if 0 <= duration < min:
            print(duration, 'сек')
        elif min <= duration < hour:
            m = duration // min
            s = duration % min
            print(f'{m} мин {s} сек')
        elif hour <= duration < day:
            h = duration // hour
            m = duration % hour // min
            s = duration % min
            print(f'{h} час {m} мин {s} сек')
        elif hour <= duration < day:
            d = duration // day
            h = duration % day // hour
            m = duration % day % hour // min
            s = duration % min
            print(f'{d} дн {h} час {m} мин {s} сек')
        else:
            y = duration // year
            d = duration % year // day
            h = duration % year % day // hour
            m = duration % year % day % hour // min
            s = duration % min
            print(f'{y} г {d} дн {h} час {m} мин {s} сек')
except ValueError:
    print(duration, ' - это не число')
