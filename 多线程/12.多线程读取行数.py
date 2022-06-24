# coding=gbk
# encoding='UTF-8'

import threading
import csv
import os

class MyThreadLine(threading.Thread):
    def __init__(self,path):
        threading.Thread.__init__(self)# 父类初始化
        self.path = path #路径
        self.line = -1 #统计行数
    def run(self):
        reader =csv.reader(open(self.path,"r"))#读取文件
        lines =0
        for item in reader:  #读取每一行
            lines+=1
        self.line =lines #保存行数

path= "D:\\code\\工作脚本\\quanmin\\全民所有cookie"
filelist =os.listdir(path) # 存储所有的文件名
threadlist = []#线程列表
for filename in filelist:
    newpath = path +"\\"+filename #代表完整路径
    mythd = MyThreadLine(newpath)#创建线程类对象
    mythd.start()#线程开始干活
    threadlist.append(mythd)#增加线程到线程列表
for mythd in threadlist:#遍历每一个线程
    mythd.join()#等待所有的线程干完活
linelist =[]
for mythd in threadlist:
    linelist.append(mythd.line)
print(linelist)



