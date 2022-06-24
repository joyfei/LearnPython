
class Student:
    def __init__(self,name,age):
        # 创建私有属性
        self.__name = name
        self.__age = age

    #获取私有属性
    @property
    def name(self):
        return self.__name

    #修改私有属性
    @name.setter
    def name(self,name):
        self.__name=name or '无名氏'

    #获取私有属性
    @property
    def age(self):
        return self.__age

    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}')



# stu=Student('张三',18)
# stu.study('python')
#
# print(stu._Student__name)

# python中可以通过property装饰器为’私有‘属性提供读取和修改的方法，之前我们提到过，装饰器通常会放在类，函数或方法的声明之前，
# 通过@符号表示将装饰器应用于类，函数或方法

stu=Student('固安',18)

print(stu.name,stu.age)

stu.name=''

print(stu.name)