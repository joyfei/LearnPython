import _thread  # 多线程
import time

def go():
    for i in range(10):
        print(i,"-------")
        time.sleep(1)

for i in range(5): # 50秒
    _thread.start_new_thread(go,())

for i in range(12):
    time.sleep(1)
print(" game over")