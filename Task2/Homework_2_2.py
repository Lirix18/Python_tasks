#  Задача 2 и 3* без использования новых списков и учитывая знак температуры

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-1', 'градусов']

result = ''
for i in list:
    if i.isalpha():
        result += f'{i} '
    elif i.isdigit():
        result += f'"{int(i):02d}" '
    elif i.find('+') != -1:
        result += f'"+{int(i):02d}" '
    elif i.find('-') != -1:
        result += f'"-{abs(int(i)):02d}" '

print(result)
