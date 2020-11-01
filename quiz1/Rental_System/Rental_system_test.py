from Rental_system import *

rental_system = RentalSystem(bike_numbers=13, motorcycle_numbers=14)

customer1 = Customer(1, 'mohammad', 'mirmoosavi')
customer2 = Customer(2, 'ashkan', 'divband')
customer3 = Customer(3, 'test', 'test2')

vehicle1 = customer1.request_vehicle(rental_system, 'bike', 'mountain')
customer1.return_vehicle(rental_system, vehicle1)
customer2.request_vehicle(rental_system, 'bike', 'mountain')
customer3.request_vehicle(rental_system, 'bike', 'mountain')
vehicle2 = customer1.request_vehicle(rental_system, 'bike', 'mountain')
customer1.return_vehicle(rental_system, vehicle2)

print(customer1.bill)
for elem in rental_system.rented_vehicles:
    print(elem)
