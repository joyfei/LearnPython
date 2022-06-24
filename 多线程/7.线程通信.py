## coding=gbk
import threading
import time


def goevent():
    e = threading.Event()#事件
    def go():
        for i in range(10):
            e.wait()# 等待
            e.clear() # 重置
            print("go")
    threading.Thread(target=go).start()# 开启一个线程
    return e

t=goevent()
for i in range(10):
    time.sleep(i)
    print(i)
    t.set()# 激发线程