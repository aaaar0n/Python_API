import random

wheels = [2, 4, 10]
brand = ['Toyota', 'BMW', 'Nissan', 'Mercedes-Benz', 'Honda']
color = ['blue', 'red', 'green', 'black', 'white', 'orange']
vehicle_type = ['sedan', 'motorcycle', 'truck', 'SUV', 'sports car', 'pickup']

class Vehicle:
    def create_vehicle(self):
        random_wheels = random.choice(wheels)
        random_brand = random.choice(brand)
        random_color = random.choice(color)
        if random_wheels == 2:
            random_type = "motorcycle"
        elif random_wheels == 10:
            random_type = "truck"
        else:
            random_type = random.choice(vehicle_type)
        random_car = f'{random_wheels} - {random_brand} - {random_color} - {random_type}'
        return random_car


vehicle = Vehicle()
print(vehicle.create_vehicle())
