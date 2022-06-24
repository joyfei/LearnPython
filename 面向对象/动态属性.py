class Student:
    # 如果当前的类不允许开发者进行动态属性添加
    # __slots__ = ('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age = age



stu = Student('固安',20)

# 想要在不修改当前类的代码的情况下，去添加一个属性
stu.sex ='男'
print(stu.name,stu.age,stu.sex)
