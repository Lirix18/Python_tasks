prices = [57.8, 46.51, 97, 28.45, 55, 0.15, 76, 0.99, 1, 150, 34.1, 34.01, 34.6]


# функция добавления в вывод руб и коп
def rr_kk(list):
    res = []
    for i in list:
        if type(i) == int:
            res.append(f'{i} руб 00 коп')
        elif int(i) > 0:
            k = str(i).split(".")[-1]
            if len(k) > 1:
                res.append(f'{int(i)} руб {int(k):02d} коп')
            else:
                res.append(f'{int(i)} руб {int(k)}0 коп')
        else:
            res.append(f'{str(i).split(".")[-1]} коп')
    return res


# список цен с руб и коп
print('id списка цен ', id(prices))
print(*rr_kk(prices), sep=', ')

prices.sort()

# сортированный по возрастанию список цен с руб и коп
print('id сортированного списка по возрастанию цен ', id(prices))
print(*rr_kk(prices), sep=', ')

prices_r = sorted(prices, reverse=True)

# сортированный по убыванию список цен с руб и коп
print('id сортированного по убыванию списка цен ', id(prices_r))
print(*rr_kk(prices_r), sep=', ')

# Список 5 самых высоких цен
print(*rr_kk(prices_r[:5]), sep=', ')
