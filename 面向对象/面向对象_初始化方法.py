class Student:
    def __init__(self,name,age):
        # 给当前类添加属性
        self.name = name
        self.age = age

    def study(self,course_name):
        # 属性使用self进行调用 参数是直接调用
        print(f'{self.name}正在学习{course_name}')

    def play(self):
        print(f'{self.name}正在玩游戏')

    #使用类中内置的魔术方法来实现
    def __repr__(self):
        return f'{self.name}:{self.age}'

#实例化类

stu1 = Student('固安',18)

#打印当前对象
print(stu1)

stu1.study('python')

stu2 =Student('夏洛',20)

stu2.play()


