class Car :
    def __init__ (self,make,model,year):

        self.make = make
        self.model = model
        self.year = year
        self.odmoeter = 2

    def get_descriptive_name (self):
        long_name = f"{self.make} {self.year} {self.model} {self.odmoeter}"
        return long_name
    def update_odmoeter(self,milage):
        if milage >= 0 :
            self.odmoeter += milage
        else:
            print("WARNING！你没有权限执行该操作")

my_new_car = Car("奥迪","A6","2021")
print(my_new_car.get_descriptive_name())
my_new_car.update_odmoeter(10)
print(my_new_car.get_descriptive_name())
