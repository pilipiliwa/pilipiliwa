"""一个用来描述汽车的类"""
class Car :
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回简洁描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条消息，指出汽车里程"""
        print(f"这辆车已经行驶了{self.odometer_reading}公里")

    def update_odometer(self,mileage):
        """里程表读数设置为指定值，不允许回退"""
        if mileage >= self.odometer_reading:
            self.odometer_reading =mileage
        else:
            print ("错误参数，请重试！")
    

    def increment_odometer(self,miles):
        self.odometer_reading += miles