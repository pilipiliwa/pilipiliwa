class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print(f"水池里 有乌龟{self.turtle.num}只，有鱼{self.fish.num}条")
my_fool = Pool(22,33)
my_fool.print_num()
  ##https://www.bilibili.com/video/BV1Fs411A7HZ?p=40