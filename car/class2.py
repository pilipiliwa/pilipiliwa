class Dog :
    ##创建一个类 “狗”
    def __init__(self,name,age) : ##形参“self”必不可少，且必须位于其他形参前面
        ##这个是一个 特殊方法（_init_）（必不可少）
        ##下边是两个属性 name 和 age
        self.name = name  ##self.xx 可被类中所有方法使用
        self.age = age
    ##接下来是自己定义的方法
    def sit(self):
        print(f"{self.name}坐下了")
    def roll_over(self):
        print(f"{self.name}打了个滚")

    """
        参数调用关系：
                    my_dog = Dog("史密斯",55) 这里的“史密斯”指向形参 name，_init_方法中的属性 self.name = name将“史密斯”传给self.name
                    def 函数sit(self)中   
                        print(f"{self.name}坐下了") 调用到“史密斯”


    """
my_dog = Dog("史密斯",55)
your_dog = Dog("大黄",11)
dog_1 = your_dog
s = my_dog
print (f"我的狗叫{s.name}")   ## 访问类中属性
print (f"我的狗现在{s.age}岁了")
s.sit() ## 调用类中方法
s.roll_over()