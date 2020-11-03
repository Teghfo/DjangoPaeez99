import random
from random import randint


class RentalSystem:
    def __init__(self, bike_numbers=20, motorcycle_numbers=10):
        self.bike_numbers = bike_numbers
        self.motorcycle_numbers = motorcycle_numbers
        self.bikes = []
        self.motorcycles = []
        self.mountain_bikes = 0
        self.street_bikes = 0
        self.electric_motorcycle = 0
        self.engine_motorycyle = 0
        self.id_set = [i for i in range(1, bike_numbers + motorcycle_numbers)]
        self.initialize_bikes_motorcycles()
        self.rented_vehicles = []

    def initialize_bikes_motorcycles(self):

        for i in range(self.bike_numbers):
            bike_kind = random.choice(Bike.BIKE_KINDS)
            base_price = randint(50, 100)
            self.bikes.append(Bike(self.id_set[i], base_price, bike_kind))

        for i in range(self.motorcycle_numbers):
            motorcycle_kind = random.choice(MotorCycle.MOTORCYCLE_KINDS)
            base_price = randint(100, 200)
            self.motorcycles.append(MotorCycle(self.id_set[i], base_price, motorcycle_kind))

    def available_vehicle(self, vehicle_type, vehicle_kind):
        if vehicle_type == 'bike':
            for vehicle in self.bikes:
                if vehicle not in self.rented_vehicles and vehicle.kind == vehicle_kind:
                    self.rented_vehicles.append(vehicle)
                    return [True, vehicle]
            print('there is no bikes with your condtions')
            return [False, None]
        elif vehicle_type == 'motorcycle':
            for vehicle in self.motorcycles:
                if vehicle not in self.rented_vehicles and vehicle.kind == vehicle_kind:
                    self.rented_vehicles.append(vehicle)
                    return [True, vehicle]
            print('there is no motor with your condtions')
            return [False, None]
        else:
            print('you enter wrong information')
            return [False, None]

    def return_vehicle(self, vehicle_id):
        for vehicle in self.bikes:
            if vehicle.id == vehicle_id:
                self.rented_vehicles.remove(vehicle)
                return vehicle
        for vehicle in self.motorcycles:
            if vehicle.id == vehicle_id:
                self.rented_vehicles.remove(vehicle)
                return vehicle
        return None


class Vehicle:
    def __init__(self, id, rent_price):
        self.id = id
        self.rent_price = rent_price


class Bike(Vehicle):
    BIKE_KINDS = ('mountain', 'street')

    def __init__(self, id, rent_price, kind):
        super().__init__(id, rent_price)
        if kind not in Bike.BIKE_KINDS:
            raise Exception('wrong kind')
        self.kind = kind

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.rent_price, self.kind)


class MotorCycle(Vehicle):
    MOTORCYCLE_KINDS = ('electric', 'engine')

    def __init__(self, id, rent_price, kind):
        super().__init__(id, rent_price)
        if kind not in MotorCycle.MOTORCYCLE_KINDS:
            raise Exception('wrong kind')
        self.kind = kind

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.rent_price, self.kind)


class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.bill = 0
        self.vehicle = None

    def request_vehicle(self, rental_system, vehicle_type, vehicle_kind):
        vehicle_status, vehicle = rental_system.available_vehicle(vehicle_type, vehicle_kind)

        if vehicle_status:
            print('customer {} vehicle is: {}'.format(self.id, str(vehicle)))
            self.vehicle = vehicle
            return vehicle.id
        return None

    def return_vehicle(self, rental_system, vehicle_id):
        vehicle = rental_system.return_vehicle(vehicle_id)
        if vehicle:
            self.bill += vehicle.rent_price
            print('your vehicle {}  is pay back and sum of your bill is {} '.format(str(vehicle), self.bill))
            return
        print('there is no vehicle to pay back')
