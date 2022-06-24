class Animal:
    def eat(self):

        print('吃')

    def drink(self):

        print('喝')

    def run(self):

        print('跑')

    def sleep(self):

        print('睡')
#狗类
class Dog(Animal):

    def bark(self):

        print('汪汪叫')
#哮天犬类
class Xiaotian(Dog):
    def fly(self):
        print('我会飞')

class Cat(Animal):
    def bark(self):
        print('喵喵喵')

xtq = Xiaotian()

xtq.fly()

mc=Cat()

mc.run()