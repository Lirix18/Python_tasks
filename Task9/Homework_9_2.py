class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def math(self, weight, thickness):
        calc = (self._lenght * self._width * weight * thickness) / 1000
        return f'{calc} т'


road1 = Road(5000, 20)
print(road1.math(25, 5))

road2 = Road(1250, 35)
print(road2.math(25, 5))