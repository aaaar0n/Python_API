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
    wheels = '2'
    


motorcycle = Motorcycle()
print(motorcycle.create_vehicle())
# print(motorcycle.create_vehicle())

# motorcycle = Motorcycle()
# motorcycle.__init__()
# print(motorcycle.create_vehicle())

    











# class Motorcycle(Vehicle)
#     wheels = 2


#         if random_wheels == 2:
#             random_type = "motorcycle"
#         elif random_wheels == 10:
#             random_type = "truck"
#         else:
#             random_type = random.choice(vehicle_type)
#         random_car = f'{random_wheels} - {random_brand} - {random_color} - {random_type}'
#         return random_car


# vehicle = Vehicle()
# print(vehicle.create_vehicle())
