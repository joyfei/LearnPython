import threading,time
ticket =100
def sell_ticket():
    global ticket
    while True:
        if ticket>0:
            time.sleep(1)
            ticket -=1
            print('{}卖出一张票，还剩{}张'.format(threading.current_thread().name,ticket))
        else:
            print("票卖完了")
            break

t1 = threading.Thread(target=sell_ticket,name="线程一")
t2 = threading.Thread(target=sell_ticket,name="线程二")
t3 = threading.Thread(target=sell_ticket,name="线程三")
t4 = threading.Thread(target=sell_ticket,name="线程四")
t1.start()
t2.start()
t3.start()
t4.start()