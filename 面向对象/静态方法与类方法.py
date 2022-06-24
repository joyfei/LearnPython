
class Triangle(object):
    def __init__(self,a,b,c):
        # 创建私有属性
        self.a = a
        self.b = b
        self.c = c

    #装饰器
    @staticmethod
    def is_valid(a,b,c):
        #判断三条边长能否构成三角形（静态方法）
        return a +b > c and b + c > a and a + c > b

    def perimeter(self):
        #计算周长
        return self.a+self.b+self.c

#通过调用类计算三角形的周长

tri = Triangle(3,4,5)

print(tri.perimeter())

# 在调用静态方法时，不需要对当前类进行实例化可以直接使用类名方法

# 类方法的参数第一位必须是cls class 代表当前的方法属于当前的类

#静态方法时不和当前类进行绑定的 可以看成一个单独的函数
print(Triangle.is_valid(1,1,5))


