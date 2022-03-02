names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# через новый список
for i in names:
    list = i.split()
    list[-1] = list[-1].title()
    print(f'Привет, {list[-1]}!')

# без списка
for i in names:
    name = i.split()[-1].title()
    print(f'Привет, {name}!')


