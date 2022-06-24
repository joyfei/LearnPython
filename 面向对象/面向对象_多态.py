class A:
    def work(self):
        print('人类要工作')

class B(A):
    def work(self):
        print('程序员在工作--代码')


class C(A):
    def work(self):
        print('程序员在工作--代码')

b=B()
c=C()

b.work()
c.work()
