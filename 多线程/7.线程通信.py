## coding=gbk
import threading
import time


def goevent():
    e = threading.Event()#�¼�
    def go():
        for i in range(10):
            e.wait()# �ȴ�
            e.clear() # ����
            print("go")
    threading.Thread(target=go).start()# ����һ���߳�
    return e

t=goevent()
for i in range(10):
    time.sleep(i)
    print(i)
    t.set()# �����߳�