# create a car class with arttributes like brand and model. Then create an instance of the class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.brand)
print(my_car.model)
