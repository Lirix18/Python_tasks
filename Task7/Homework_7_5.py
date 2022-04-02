import os
import json

"""Очень интересное задание, пришлось покопаться"""
def stats(root):
    stat = {}
    for roots, dirs, files in os.walk(root):
        for file in files:
            current_file = os.path.join(roots, file)  # путь к файлу
            size = os.stat(current_file).st_size  # размер файла
            key = 10 ** len(str(size))  # ключ файла - его размер
            file_extend = current_file.split('.')[-1]  # расширение файла
            count, extends = stat.get(key, (0, []))  # задаем значение count и extends, далее считываем их из словаря
            extends.append(file_extend)  # добавляем в список расширение
            extends = list(set(extends))  # оставляем только уникальные расширения
            count += 1  # прибавляем счетчик файлов
            stat[key] = (count, extends)  # добавляем в словарь, при необходимости меняем с новым значением
    if stat == {}:
        raise Exception('В директории нет файлов')  # вызываем ошибочку
    return stat


def print_stat(root):
    """Сортируем по ключу и выводим"""
    statistic = sorted(stats(root).items(), key=lambda x: x[0])
    print(dict(statistic))
    # print('~' * 10, 'Выводим поэлементно', '~' * 10)
    # for key, value in dict(statistic).items():
    #     print({key: (value[0], list(value[1]))})


with open('stat.txt', 'w', encoding='utf-8') as file:
    json.dump(stats(os.getcwd()), file)


if __name__ == '__main__':
    try:
        folder1 = './'
        folder2 = 'my_project'
        folder3 = '123'
        print_stat(folder1)
        print('~' * 25)
        print_stat(folder2)
        print('~' * 25)
        print_stat(folder3)
    except Exception as e:
        print(e)
