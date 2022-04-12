class Stationery:
    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Пишем {self._title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {self._title} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Пишем {self._title} маркером')


pen = Pen('Red pen')
pen.draw()
pencil = Pencil('Зеленый карандаш')
pencil.draw()
handle = Handle('Black Handle')
handle.draw()
