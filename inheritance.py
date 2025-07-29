class Vehicle:
    def __init__(self, n_wheels, hp, n_seats, color):
        self.n_wheels = n_wheels
        self.hp = hp
        self.n_seats = n_seats
        self.color = color
    def getColor(self):
        return self.color
    def getCurrentSpeed(self):
        return 114514
    def getSeats(self):
        return self.n_seats

class Car(Vehicle):
    def __init__(self, n_wheels, hp, n_seats, color, plate):
        super().__init__(n_wheels, hp, n_seats, color)
        self.plate = plate
    def getCurrentSpeed(self):
        return 120
    def getPlate(self):
        return self.plate

class Bike(Vehicle):
    def __init__(self, n_wheels, hp, n_seats, color):
        super().__init__(n_wheels, hp, n_seats, color)
    def getCurrentSpeed(self):
        return 25
    
genericVehicle = Vehicle("no idea tbh", "no idea", "idk", "stop asking")
print(f"I'm going {genericVehicle.getCurrentSpeed()} kilometers per hour.")
print(f"My color is {genericVehicle.getColor()}.")
print(f"I have {genericVehicle.getSeats()} seats.")

print()

car = Car(4, 1000, 5, "blue", "京A88888")
print(f"I'm going {car.getCurrentSpeed()} kilometers per hour.")
print(f"My color is {car.getColor()}.")
print(f"I have {car.getSeats()} seats.")
print(f"My plate number is {car.getPlate()}.")

print()

bike = Bike(2, 0, 1, "black")
print(f"I'm going {bike.getCurrentSpeed()} kilometers per hour.")
print(f"My color is {bike.getColor()}.")
print(f"I have {bike.getSeats()} seats.")
