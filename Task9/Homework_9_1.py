import time


class TrafficLight:
    def __init__(self, color='red'):
        self.__color = color

    def running(self):
        for i in range(10):
            if self.__color == 'red':
                print('RED')
                time.sleep(7)
                self.__color = 'yellow'
            elif self.__color == 'yellow':
                print('YELLOW')
                time.sleep(2)
                self.__color = 'green'
            else:
                print('GREEN')
                time.sleep(5)
                self.__color = 'red'


traffic = TrafficLight()
traffic.running()





