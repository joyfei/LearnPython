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
    #重写父类方法
    def bark(self):
        #z在当前方法中去调用父类方法
        #使用super方法
        print('神狗叫')

        #super也是一个对象
        # super().bark()

        #另一种调用方法
        Dog.bark(self)

        #在当前代码中通过子类.方法的方式去调用方法
        #递归循环 --死循环
        Xiaotian.bark(self)

        #当前子类方法进行拓展
        print('这是一个测试。。。。。')

xtq=Xiaotian()
xtq.bark()