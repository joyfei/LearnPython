# coding=gbk

import time
import threadpool

"""
   ����̼߳�������

"""



def show(str):
    print("hello",str)
    time.sleep(2)

namelist=["gaosdf","sfdf","sdfdfs"]



start_time =time.time()# ��ʼʱ��
pool = threadpool.ThreadPool(10)#�������10��
requests = threadpool.makeRequests(show,namelist)
for req in requests:
    pool.putRequest(req)
end_time = time.time()
print(end_time-start_time)