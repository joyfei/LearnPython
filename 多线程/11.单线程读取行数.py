# coding=gbk
import threading
import csv

class MyThreadLine(threading.Thread):
    def __init__(self,path):
        threading.Thread.__init__(self)# 父类初始化
        self.path = path #路径
        self.line = -1 #统计行数
    def run(self):
        reader =csv.reader(open(self.path,"r"))#读取文件
        lines =0
        for item in reader:#读取每一行
            lines+=1
        self.line =lines #保存行数


path= r"C:\Users\Administrator\Desktop\新建文本文档.csv"
mythd =MyThreadLine(path)
mythd.start()
mythd.join()
print(mythd.line)
