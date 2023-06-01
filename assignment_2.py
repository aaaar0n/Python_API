import random

class Vehicle:
    wheels = ''

    def __init__(self):
        self.wheels = [2, 4, 10]
        self.brand = ['Toyota', 'BMW', 'Nissan', 'Mercedes-Benz', 'Honda']
        self.color = ['blue', 'red', 'green', 'black', 'white', 'orange']
        self.vehicle_type = ['sedan', 'motorcycle', 'truck', 'SUV', 'sports car', 'pickup']

    def create_vehicle(self):
        random_brand = random.choice(self.brand)
        random_color = random.choice(self.color)
        random_type = random.choice(self.vehicle_type)
        random_vehicle_no_wheels = random_brand + ' ' + random_color + ' ' + random_type
        return f'{random_vehicle_no_wheels}'


class Motorcycle(Vehicle):
    def show_wheels(self):
        wheels = '2'
        return wheels


class Truck(Vehicle):
    def show_wheels(self):
        wheels = '10'
        return wheels


class car(Vehicle):
    def show_wheels(self):
        wheels = '4'
        return wheels

motorcycle = Motorcycle()
random_motorcycle = motorcycle.create_vehicle()
print(f'{random_motorcycle} {motorcycle.show_wheels()}')

