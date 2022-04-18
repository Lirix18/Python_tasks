import re


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def type_int(cls, date):
        try:
            day, month, year = [int(i) for i in date.split('-')]
            return f'{type(day), day}, {type(month), month}, {type(year), year}'
        except ValueError:
            return f'Неверное значение'

    @staticmethod
    def validate(date):
        day, month, year = [int(i) for i in date.split('-')]
        if 1 < day > 32:
            raise ValueError('Wrong day')
        if 1 < month > 12:
            raise ValueError('Wrong month')
        if month in [4, 6, 9, 11] and day == 31:
            raise ValueError('Wrong day and month')
        return day, month, year


print(Date.type_int('12-04-2022'))
print(Date.validate('15-04-2022'))
print(Date.validate('31-04-2022'))
