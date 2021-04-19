class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        from time import sleep
        times = {'красный': 2,
                 'желтый': 2,
                 'зеленый': 2
                 }
        print('Press Control+C to interrupt')
        try:
            while True:
                if self.__color == 'красный':
                    print('Горит красный свет')
                    sleep(times['красный'])
                    self.__color = 'желтый'
                elif self.__color == 'желтый':
                    print('Горит желтый свет')
                    sleep(times['желтый'])
                    self.__color = 'зеленый'
                else:
                    print('Горит зеленый свет')
                    sleep(times['зеленый'])
                    self.__color = 'красный'
        except KeyboardInterrupt:
            pass


a = TrafficLight('зеленый')
a.running()
