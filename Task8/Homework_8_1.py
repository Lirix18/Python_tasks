import re


def email_parse(email):
    parse_email = re.compile(r'(?P<key>[A-Za-z0-9\.\-\_]+)@(?P<value>([A-Za-z0-9]+\.[A-Z|a-z]{2,})+)', re.IGNORECASE)
    if parse_email.match(email):
        print(*map(lambda x: x.groupdict(), parse_email.finditer(email)))
    else:
        raise ValueError('Неверный адрес')


if __name__ == '__main__':
    email1 = 'someone@Geekbrains.ru'
    email2 = 'someone@geekbrainsru'
    email_parse(email1)
    email_parse(email2)
