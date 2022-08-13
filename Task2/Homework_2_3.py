# программа без списка и с учетом знака градусов

list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']

res = ''
for i in list:
    if i.isalpha():
        res += f'{i} '
    elif i.isdigit():
        res += f'"{int(i)}" '
    elif str(i).find('+') != -1:
        res += f'"+{int(i):02d}" '
    elif str(i).find('-') != -1:
        res += f'"-{abs(int(i)):02d}" '

print(res)
