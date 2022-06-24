## coding=gbk
import threading
import time


def goevent():
    e = threading.Event()#事件
    def go():
        e.wait()# 等待,等待set再执行
        e.clear()# 清理
        print("go")
    threading.Thread(target=go).start()# 开启一个线程
    return e

t=goevent()
time.sleep(5)
t.set()# 激发线程