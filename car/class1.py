##新建一个类
class Dog:
    ##  _init_ 一种方法，两侧必须有下划线
    def __init__(self, name, age):  ##三个形参 self、 name、 age
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog("lisa", 66)
print(f"My dog name is {my_dog.name}.")
my_dog.roll_over()
