## coding=gbk
import threading
import time


def goevent():
    e = threading.Event()#�¼�
    def go():
        e.wait()# �ȴ�,�ȴ�set��ִ��
        e.clear()# ����
        print("go")
    threading.Thread(target=go).start()# ����һ���߳�
    return e

t=goevent()
time.sleep(5)
t.set()# �����߳�