class A:
    def test(self):
        print('test 方法')

class B:
    def demo(self):
        print('demo 方法')

class C(A,B):
    pass

c=C()
c.test()
c.demo()


"""
在python中 面向对象是支持多个类进行继承的
子类同时具有父类中的所有的方法和属性
 
"""