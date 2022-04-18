class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Input a: '))
    b = int(input('Input b: '))
    if b == 0:
        raise OwnError(" Don't do it! It's danger!")
    print(f'{a}/{b} = {a/b}')
except OwnError as e:
    print(e)