class Car:
    TOTAL_WHEEL = 4

    def __init__(self):
        Car.TOTAL_WHEEL = Car.TOTAL_WHEEL + 1

    @classmethod
    def total_wheels(cls):
        print(f'Total wheels: {cls.TOTAL_WHEEL}')


car_1 = Car()
car_2 = Car()
car_3 = Car()

Car.total_wheels()
