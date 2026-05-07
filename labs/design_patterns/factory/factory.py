
class VehicleFactory:
    
    @staticmethod
    def create_vehicle(vehicle_type: str, brand: str, model: str):
        if vehicle_type == "car":
            vehicle = Car(brand, model, doors=4)
        elif vehicle_type == "motorcycle":
            vehicle = Motorcycle(brand, model, engine_type="V-Twin-Turbo")
        elif vehicle_type == "truck":
            vehicle = Truck(brand, model, cargo_capacity=1000)
        elif vehicle_type == "bus":
            vehicle = Bus(brand, model, seat_count=30)
        else: 
            raise ValueError("Unknown type")
        
        return vehicle



class Car:
    def __init__(self, brand, model, doors):
        self._brand = brand
        self._model = model
        self._doors = doors
        self._rental_rate = 50 # dollars
    
    def start_engine(self):
        return f"{self._brand} {self._model} engine started"


class Motorcycle:
    def __init__(self, brand, model, engine_type):
        self._brand = brand
        self._model = model
        self._engine_type = engine_type
        self._rental_rate = 30 # dollars
    
    def start_engine(self):
        return f"{self._brand} {self._model} ({self._engine_type}) engine started"


class Truck:
    def __init__(self, brand, model, cargo_capacity):
        self._brand = brand
        self._model = model
        self._cargo_capacity = cargo_capacity
        self._rental_rate = 100 # dollars
    
    def start_engine(self):
        return f"{self._brand} {self._model} (capacity {self._cargo_capacity}L) engine started"


class Bus:
    def __init__(self, brand, model, seat_count):
        self._brand = brand
        self._model = model
        self._seat_count = seat_count
        self._rental_rate = 100 # dollars
    
    def start_engine(self):
        return f"{self._brand} {self._model} (seat count {self._seat_count}) engine started"
    


vehicle_type = input("What type of vehicle you would like to rent?(car/motorcycle/truck):")
brand = "Toyota"
model = "Camry"

vehicle = VehicleFactory.create_vehicle(vehicle_type, model, brand)

print(vehicle.start_engine())
print(f"Rental rate: {vehicle._rental_rate}/day")




# def rent_vehicle(vehicle_type):
#     if vehicle_type == "car":
#         vehicle = Car(brand, model, doors=4)
#     elif vehicle_type == "motorcycle":
#         vehicle = Motorcycle(brand, model, engine_type="V-Twin-Turbo")
#     elif vehicle_type == "truck":
#         vehicle = Truck(brand, model, cargo_capacity=1000)
#     elif vehicle_type == "bus":
#         vehicle = Bus(brand, model, seat_count=30)
#     else: 
#         raise ValueError("Unknown type")
#     print(f"vehicle {vehicle._brand} {vehicle._model} {vehicle._rental_rate} was rented")


# def get_vehicle_price(vehicle_type):
#     if vehicle_type == "car":
#         vehicle = Car(brand, model, doors=4)
#     elif vehicle_type == "motorcycle":
#         vehicle = Motorcycle(brand, model, engine_type="V-Twin-Turbo")
#     elif vehicle_type == "truck":
#         vehicle = Truck(brand, model, cargo_capacity=1000)
#     elif vehicle_type == "bus":
#         vehicle = Bus(brand, model, seat_count=30)
#     else: 
#         raise ValueError("Unknown type")
#     return vehicle._rental_rate

# def process_return(vehicle_type, number_of_days):
#     if vehicle_type == "car":
#         vehicle = Car(brand, model, doors=4)
#     elif vehicle_type == "motorcycle":
#         vehicle = Motorcycle(brand, model, engine_type="V-Twin-Turbo")
#     elif vehicle_type == "truck":
#         vehicle = Truck(brand, model, cargo_capacity=1000)
#     elif vehicle_type == "bus":
#         vehicle = Bus(brand, model, seat_count=30)
#     else: 
#         raise ValueError("Unknown type")

#     print(f"Your total: {vehicle._rental_rate * number_of_days}")


def rent_vehicle(vehicle_type):
    vehicle = VehicleFactory.create_vehicle(vehicle_type)
    print(f"vehicle {vehicle._brand} {vehicle._model} {vehicle._rental_rate} was rented")


def get_vehicle_price(vehicle_type):
    vehicle = VehicleFactory.create_vehicle(vehicle_type)
    return vehicle._rental_rate

def process_return(vehicle_type, number_of_days):
    vehicle = VehicleFactory.create_vehicle(vehicle_type)
    print(f"Your total: {vehicle._rental_rate * number_of_days}")
