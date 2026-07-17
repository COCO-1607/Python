# modify the Car class to encapsulate the brand attribute , making it private, and provide getter methods for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
            return self.__brand + "!"
        
    def full_name(self):
             return f"{self.__brand}{self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model S", 100)
# print(my_electric_car.__brand)
print(my_electric_car.get_brand())

    