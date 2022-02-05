class Car :
    def __init__ (self,make,model,year):

        self.make = make
        self.model = model
        self.year = year
        self.odmoeter = 2
        self.gas_tank_L = 50
    def get_descriptive_name (self):
        long_name = f"{self.year}{self.make}{self.model},{self.odmoeter}"
        return long_name.title()
    def update_odmoeter(self,milage):
        if milage >= 0 :
            self.odmoeter += milage
        else:
            print("WARNING！你没有权限执行该操作")
    def gas_tank_size(self):
        print(self.gas_tank_L)
"""
yy_car =Car("奥迪","A6",2021)
print(yy_car.gas_tank_size())
                            """


class Battery:
    def __init__(self,battery,battery_size=75):
        self.battery_size = battery_size
        self.battery = battery
        
    def describe_battery(self):
        print (f"the battery was made for {self.battery}")
    
    def describe_battery_size(self):
        print(f"the car have {self.battery_size} -kwh battery")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  ##为啥呢
    def gas_tank(self):
        pass
    
my_car = ElectricCar("tesla","models",1010)
print(my_car.gas_tank())
print(my_car.get_descriptive_name())
