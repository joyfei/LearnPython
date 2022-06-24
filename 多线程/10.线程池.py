# coding=gbk

import time
import threadpool

"""
   解决线程加速问题

"""



def show(str):
    print("hello",str)
    time.sleep(2)

namelist=["gaosdf","sfdf","sdfdfs"]



start_time =time.time()# 开始时间
pool = threadpool.ThreadPool(10)#最大容量10个
requests = threadpool.makeRequests(show,namelist)
for req in requests:
    pool.putRequest(req)
end_time = time.time()
print(end_time-start_time)