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



class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print ("the battery was made for ")
    
    def describe_battery_size(self):
        print(f"the car has a {self.battery_size} -kwh battery")
        
    def get_range(self):
        if self.battery_size == 75 :
            range = 260
        else :
            range = 315
        print (f"This car can go about {range} miles on a full range")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def gas_tank(self):
        pass

my_tesla = ElectricCar("tesla","model",2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery_size())
