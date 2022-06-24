import threading

def dance():
    for i in range(5):
        print("我正在跳舞",i)



def singe():
    for i in range(5):
        print("我正在唱歌",i)

t1 = threading.Thread(target=dance)
t2 = threading.Thread(target=singe)
t1.start()
t2.start()
