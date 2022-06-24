class A:
    #创建类属性
    def __init__(self):
        # 公有属性
        self.num_1 = 100
        # 私有属性
        self.__num_2 = 200
    # 创建私有方法
    def __test(self):
        print(f'私有属性与公有属性的值:{self.num_1},{self.__num_2 }')

    # 公有方法
    def test(self):
        print(f'父类中的公有方法输出私有属性：{self.__num_2}')
        #在公有方法中调用私有方法
        self.__test()

class B(A):
    # 公有方法
    def demo(self):
        #1.在子类方法中访问父类的公有属性

        print(f'子类方法输出父类的公有方法输出私有属性')

        #2.在子类中调用父类的公有方法输出私有属性

        self.test()

b=B()
b.demo()

"""
子类可以通过父类的公有方法简单访问到私有属性和私有方法


"""