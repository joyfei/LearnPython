class Student:
    #如果函数在在类中 那么被称为类方法
    def study(self,course_name):
        print(f'学生正在学习{course_name}')

    def play(self):
        print('学生正在玩游戏')


# 当前的stu Student这个类的对象 是一个具体实例
stu = Student()

# 当前输出的值为这个具体实例在内存中的地址 十六进制的值

# print(stu)
#
# print(hex(id(stu)))

#通过类.方法去调用类中的方法

stu.study('python 程序设计')
#需要对当前的类进行实例化
# Student.study('java')

Student().study('java')

"""
 想要去调用当前类中的方法
        首先需要对当前的类进行实例化
"""