class IntError(ValueError):
    def __init__(self, txt):
        self.txt = txt


spisok = []
while True:
    try:
        answer = input(f'Input number or "stop" for quit').lower()
        if answer == 'stop':
            print(spisok)
            break
        elif not answer.isdigit():
            raise IntError('Only numbers')
        spisok.append(int(answer))
    except IntError as e:
        print(e.txt)
