# test10.py

import random
clovers=['클로버1','클로버2','클로버3']
print(random.sample(clovers,2))

print('------------')

class Car:
    def __init__(self, wheel, price):
        self.wheel=wheel
        self.price=price
        
car = Car(4, 3000)
print(car.wheel)
print(car.price)

print('------------')

class Bicycle(Car):
    def __init__(self, year, wheel, price):
        self.year=year
        super().__init__(wheel, price)

bicycle = Bicycle(2021, 2, 100)
print(bicycle.year)
print(bicycle.wheel)
print(bicycle.price)

print('------------')

class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year=year
        super().__init__(wheel, price)
        self.drivetrain = drivetrain

bicycle = Bicycle(2021, 2, 100, "시마노")
print(bicycle.drivetrain)

print('------------')

class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year=year
        super().__init__(wheel, price)
        self.drivetrain = drivetrain
    def info(self):
        print('year :', self.year)
        print('wheel :', self.wheel)
        print('price :', self.price)
        
bicycle = Bicycle(2021, 2, 100, "시마노")
bicycle.info()   

print('------------')

class Bicycle(Car):
    def __init__(self, year, wheel, price, drivetrain):
        self.year=year
        super().__init__(wheel, price)
        self.drivetrain = drivetrain
    def info(self):
        print('year :', self.year)
        print('wheel :', self.wheel)
        print('price :', self.price)
        print('drivetrain :', self.drivetrain)
        
bicycle = Bicycle(2021, 2, 100, "시마노")
bicycle.info()   