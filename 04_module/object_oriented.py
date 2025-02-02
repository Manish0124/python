class Car:
     
    total_car = 0

    def __init__(self,brand, model):
        self.__brand = brand    
        self.__model = model     
        Car.total_car+=1

    def get_brand(self):
        return self.__brand + "!"  

    def full_name(self):
        return f"{self.__model} {self.__brand}"

    def fuel_type(self):
        return  "petrol or diesel"   
    
    @staticmethod
    def general_description():
        return "cars are mean of transports !" 

    @property
    def model(self):
        return self.__model    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size   

    def fuel_type(self):
        return "electric charge"         

   

tesla = ElectricCar("tesla", "models", "87kwh")
# print(tesla.full_name())
# print(tesla.fuel_type())
# print(tesla.get_brand())

safari = Car("tata","safari")
# print(safari.fuel_type())

# print(safari.general_description())
# print(Car.general_description())

# print(Car.total_car)

# my_car = Car("toyta", "corolla")
# print(my_car.brand)    
# print(my_car.full_name())   

my_car = Car("tata","nexon")
# my_car.model = "nano"

print(my_car.model)



