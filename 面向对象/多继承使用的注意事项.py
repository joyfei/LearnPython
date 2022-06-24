class A:
    def test(self):
        print('A----test 方法')

    def demo(self):
        print('A----demo 方法')

class B:
    def test(self):
        print('B----test 方法')

    def demo(self):
        print('B----demo 方法')

class C(A,B):
    pass

c=C()
c.test()
c.demo()

print(C.__mro__)#查看方法顺序
"""
调用顺序和我们的继承顺序有关系

如果在多继承的情况下发现父类中的方法有重名
尽量避免使用多继承

"""