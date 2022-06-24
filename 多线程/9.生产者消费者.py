# coding=gbk
import threading
import queue
import time
import random



myqueue = queue.Queue(10) #0代表无限。10最大容量

#生产
class creatorThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index = index #索引
        self.myqueue =myqueue #列队
    def run(self):
        while True:
            time.sleep(3)#三秒生产一个
            num = random.randint(1,10000)#随机数
            self.myqueue.put("input 生产者"+str(self.index)+"硅胶娃娃"+str(num))
            print("input 生产者"+str(self.index)+"硅胶娃娃"+str(num))
        self.myqueue.task_done() # 完成任务

#消费
class creatorThread(threading.Thread):
    def __init__(self,index,myqueue):
        threading.Thread.__init__(self)
        self.index = index #索引
        self.myqueue =myqueue #列队
    def run(self):
        while True:
            time.sleep(1)
            item = self.myqueue.get()#抓取数据
            if item is None:
                break
            print("客户",self.index,"买到物品",item)
        self.myqueue.task_done() #完成任务

for i in range(3):
    creatorThread(i,myqueue).start() #生产者

for i in range(8):
    creatorThread(i,myqueue).start() #消费者