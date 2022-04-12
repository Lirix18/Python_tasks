class Worker:
    def __init__(self, name, surname, position, wade, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wade': wade, 'bonus': bonus}

    def __str__(self):
        return f'{self.name} {self.surname}, оклад: {self._income["wade"]}, премия: {self._income["bonus"]}'


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = (self._income['wade']) + (self._income['bonus'])
        return f'{result} тугриков'


worker1 = Worker('Иван', 'Иванов', 'Рыбак', 100, 35)
print(worker1)

worker2 = Position('Илья', 'Триподов', 'Менеджер', 350, 75)
print(worker2)
print(worker2.get_full_name())
print(worker2.get_total_income())