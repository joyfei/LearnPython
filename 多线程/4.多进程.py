import multiprocessing,time

def dance(n):
    for i in range(n):
        time.sleep(1)
        print("我正在跳舞")
def singe(m):
    for i in range(m):
        time.sleep(1)
        print("我正在唱歌")

if __name__ == '__main__':
    #创建两个进程
    p1 = multiprocessing.Process(target=dance,args=(20,))
    t2 = multiprocessing.Process(target=singe,args=(30,))
    p1.start()
    t2.start()