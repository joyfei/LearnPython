# coding=gbk
import threading
import queue
import time
import random



myqueue = queue.Queue(10) #0�������ޡ�10�������

#����
class creatorThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index = index #����
        self.myqueue =myqueue #�ж�
    def run(self):
        while True:
            time.sleep(3)#��������һ��
            num = random.randint(1,10000)#�����
            self.myqueue.put("input ������"+str(self.index)+"�轺����"+str(num))
            print("input ������"+str(self.index)+"�轺����"+str(num))
        self.myqueue.task_done() # �������

#����
class creatorThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index = index #����
        self.myqueue =myqueue #�ж�
    def run(self):
        while True:
            time.sleep(1)
            item = self.myqueue.get()#ץȡ����
            if item is None:
                break
            print("�ͻ�",self.index,"����Ʒ",item)
        self.myqueue.task_done() #�������

for i in range(3):
    creatorThread(i,myqueue).start() #������

for i in range(8):
    creatorThread(i,myqueue).start() #������