class Vehicle:
    def move(self):
        return "Vehicle is moved"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class bicyle(Vehicle):
    def move(self):
        return "Bicyle is pedaling"

def move(venicle):
    return venicle.move()

vehicle = Vehicle()
car = Car()
bike = bicyle()

print(vehicle.move())
print(car.move())
print(bike.move())