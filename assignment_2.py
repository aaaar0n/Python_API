import random


class Vehicle:
    """
    This is a class for vehicle.
    """

    brand = []
    color = ['blue', 'red', 'green', 'black', 'white', 'orange']
    vehicle_type = []
    wheels = 0

    def create_vehicle(self):
        """
        Docstring
        """
        random_brand = random.choice(self.brand) if self.brand else ''
        random_color = random.choice(self.color)
        random_type = random.choice(self.vehicle_type) if self.vehicle_type else ''
        created_vehicle = {
            'brand': random_brand,
            'color': random_color,
            'type': random_type,
            'wheel': self.wheels
        }
        return created_vehicle


class Car(Vehicle):
    """
    Car
    """
    brand = ['Toyota', 'BMW', 'Nissan', 'Mercedes-Benz', 'Honda']
    vehicle_type = ['sedan', 'SUV', 'sports car', 'pickup']
    wheels = 4


class Motorcycle(Vehicle):
    """
    Motor
    """
    brand = ['Russi', 'Mio', 'Click', 'Ducatti']
    vehicle_type = ['motorcyle']
    wheels = 2


class Truck(Vehicle):
    """
    Truck
    """
    brand = ['Foton', 'Volvo']
    vehicle_type = ['truck']
    wheels = [8, 10]

    def create_vehicle(self):
        """
        Docstring
        """
        random_brand = random.choice(self.brand) if self.brand else ''
        random_color = random.choice(self.color)
        random_type = random.choice(self.vehicle_type) if self.vehicle_type else ''
        random_wheel = random.choice(self.wheels) if self.wheels else 0

        created_vehicle = {
            'brand': random_brand,
            'color': random_color,
            'type': random_type,
            'wheel': random_wheel
        }
        return created_vehicle


if __name__ == '__main__':
    vehicle = Truck()
    print(vehicle.create_vehicle())
