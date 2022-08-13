import os


def stats(root):
    stat = {}
    for roots, dirs, files in os.walk(root):
        for file in files:
            current_file = os.path.join(roots, file)
            size = os.stat(current_file).st_size
            key = 10 ** len(str(size))
            count = stat.get(key, 0)
            count += 1
            stat[key] = count
    if stat == {}:
        raise Exception('В директории нет файлов')  # вызываем ошибочку
    return stat


def print_stat(root):
    """Сортируем по ключу и выводим"""
    statistic = sorted(stats(root).items(), key=lambda x: x[0])
    print(dict(statistic))


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

