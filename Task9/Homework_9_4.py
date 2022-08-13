class Car:
    def __init__(self, speed, color, name, is_police=False):
        self._speed = float(speed)
        self._color = color
        self._name = name
        self._is_police = is_police

    def __str__(self):
        return f'{self._name} {self._color} {self._speed} {self._is_police}'

    def go(self):
        return f'{self._name} on the way.'

    def stop(self):
        return f'{self._name} stopped.'

    def turn(self, direction):
        if direction == 'left':
            return f'{self._name} turn on the left.'
        elif direction == 'right':
            return f'{self._name} turn on the right.'
        else:
            raise ValueError('Wrong direction!')

    def show_speed(self):
        return f'{self._speed} km/h'


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            return f'{self._speed} km/h, you are driving too fast!'
        return f'{self._speed} km/h'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            return f'{self._speed} km/h, you are driving too fast!'
        return f'{self._speed} km/h'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True


work_car = WorkCar('40', 'green', 'Rabochaya')
print(work_car)
print(work_car.go())
print(work_car.show_speed())
print(work_car.turn('left'))
print(work_car.turn('right'))
print(work_car.stop())

town_car = TownCar('120', 'white', 'Po_gorodu')
print(town_car)
print(town_car.show_speed())

police_car = PoliceCar('150', 'white', 'Police')
print(police_car)
print(police_car.go())
