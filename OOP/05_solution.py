# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviour.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
            return self.__brand + "!"
        
    def full_name(self):
             return f"{self.__brand}{self.model}"
    
    def fuel_type(self):
          return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
          return "Electric charge"

my_electric_car = ElectricCar("Tesla", "Model S", 100)
print(my_electric_car.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

