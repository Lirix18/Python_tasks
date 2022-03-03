prices = [57.8, 46.51, 97, 35.96, 92.55, 17.09, 27, 77.1, 0.16, 42, 0.1, 150]


# функция разбиения числа на части и добавления руб и коп

def rr_kk(spisok):
    new_prices = ' '
    for i, number in enumerate(spisok):
        price = str(f"{float(number):.2f}").split(".")
        separate = ', '
        if i == len(spisok) - 1:
            separate = ''
        new_prices += (f"{price[0]} руб {price[1]} коп{separate}")
    return new_prices


# 1
id1 = id(rr_kk(prices))
print(f'id до сортировки {id(rr_kk(prices))}')
print(f'{rr_kk(prices)}')

# 2
prices.sort()

id2 = id(rr_kk(prices))
print(f'id после сортировки {id(rr_kk(prices))}')
print(f'{rr_kk(prices)}')
if id1 == id2:                                  # сравнение id списков до сортировки и после
    print('используется один и тот же список')
else:
    print('Списки разные')

# 3
new_prices = sorted(prices, reverse=True)
print(rr_kk(new_prices))

# 4
print(rr_kk(new_prices[:5]))
