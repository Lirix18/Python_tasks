import sys

argvs = sys.argv[1:]


def show_sales(argvs):
    with open('bakery.csv', 'r', encoding='utf-8') as show_file:
        if len(argvs) > 1:
            start = int(argvs[0])
            stop = int(argvs[1])
        elif len(argvs) == 0:
            start = 0
            stop = sum(1 for line in show_file)
            show_file.seek(0)
        else:
            start = int(argvs[0])
            stop = sum(1 for line in show_file)
            show_file.seek(0)

        for index, line in enumerate(show_file):
            if start <= index + 1 <= stop:
                print(line.strip())


if __name__ == "__main__":
    # show_sales('25')
    show_sales(argvs)

