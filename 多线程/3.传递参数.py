import win32api # 系统函数
import _thread  # 多线程

def show(i):
    win32api.MessageBox(0,"你的账户很危险"+str(i),"来自支付宝的问候",6)
# 顺序执行
# for i in range(5):
    # show()

for i in range(5):
    _thread.start_new_thread(show,(i,))

show(10)
