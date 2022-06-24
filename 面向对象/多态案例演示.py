class Dog():
    # 定义类属性
    def __init__(self,name):
        self.name=name

    # 方法
    def game(self):
        print('%s 在蹦蹦跳跳的玩耍。。'%self.name)

class XiaoTian(Dog):
    def game(self):
        print('%s飞到天上玩'%self.name)


class Person:
    def __init__(self,name):
        self.name=name

    def goame(self,dog):
        dog.game()
        print('%s和%s快乐的玩耍'%(self.name,dog.name))

d=XiaoTian ('旺财')

r=Person('小米')

r.goame(d)