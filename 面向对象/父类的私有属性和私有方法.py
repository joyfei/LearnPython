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



# 创建的新类要继承来自类A

class B(A):
    def demo(self):
        # 调用父类方法
        super().__test()
        # pass

"""

B 具有父类的所有属性和方法

如果是私有属性和私有方法的情况下 不可以直接去使用

"""

b=B()

# 使用子类去打印父类的公有属性
print(b.num_1)
# 使用子类去打印父类的私有属性 不可以直接打印父类的私有属性
# print(b.__num_2)

# b.__test
# 调用父类中的私有方法 不允许子类直接去调用父类私有方法的
b.demo()