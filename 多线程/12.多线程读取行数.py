# coding=gbk
# encoding='UTF-8'

import threading
import csv
import os

class MyThreadLine(threading.Thread):
    def __init__(self,path):
        threading.Thread.__init__(self)# �����ʼ��
        self.path = path #·��
        self.line = -1 #ͳ������
    def run(self):
        reader =csv.reader(open(self.path,"r"))#��ȡ�ļ�
        lines =0
        for item in reader:  #��ȡÿһ��
            lines+=1
        self.line =lines #��������

path= "D:\\code\\�����ű�\\quanmin\\ȫ������cookie"
filelist =os.listdir(path) # �洢���е��ļ���
threadlist = []#�߳��б�
for filename in filelist:
    newpath = path +"\\"+filename #��������·��
    mythd = MyThreadLine(newpath)#�����߳������
    mythd.start()#�߳̿�ʼ�ɻ�
    threadlist.append(mythd)#�����̵߳��߳��б�
for mythd in threadlist:#����ÿһ���߳�
    mythd.join()#�ȴ����е��̸߳����
linelist =[]
for mythd in threadlist:
    linelist.append(mythd.line)
print(linelist)



