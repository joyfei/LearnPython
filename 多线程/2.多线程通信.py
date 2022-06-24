import multiprocessing,time,os

def dance(n):
    for i in range(2):
        time.sleep(1)
        # print("我正在跳舞")
        # print("生产了pid{}{}".format(os.getpid(),i))
        n.put('面包')
        n.put('香肠')
def singe(m):
    for i in range(10):
        time.sleep(1)
        # print("我正在唱歌")
        print('消费了{}'.format(m.get()))

if __name__ == '__main__':
    q = multiprocessing.Queue()
    #创建两个进程
    p1 = multiprocessing.Process(target=dance,args=(q,))
    t2 = multiprocessing.Process(target=singe,args=(q,))
    p1.start()
    t2.start()