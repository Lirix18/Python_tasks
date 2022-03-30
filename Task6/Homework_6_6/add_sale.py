import sys


def add_sale(price):
    with open('bakery.csv', 'a', encoding='utf-8', newline='') as add_file:
        add_file.write(f'{price}\n')



if __name__ == "__main__":
    new_price = sys.argv[1]
    add_sale(new_price)
