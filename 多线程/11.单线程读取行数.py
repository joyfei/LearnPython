# coding=gbk
import threading
import csv

class MyThreadLine(threading.Thread):
    def __init__(self,path):
        threading.Thread.__init__(self)# �����ʼ��
        self.path = path #·��
        self.line = -1 #ͳ������
    def run(self):
        reader =csv.reader(open(self.path,"r"))#��ȡ�ļ�
        lines =0
        for item in reader:#��ȡÿһ��
            lines+=1
        self.line =lines #��������


path= r"C:\Users\Administrator\Desktop\�½��ı��ĵ�.csv"
mythd =MyThreadLine(path)
mythd.start()
mythd.join()
print(mythd.line)
