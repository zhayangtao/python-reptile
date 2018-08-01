"""
创建多线程的两种方式：
1、将一个函数传入并创建 Thread 实例，然后调用 start 方法执行；
2、从 threading.Thead 机场并创建线程，然后重写 __init__ 和 run 方法
"""

import random
import time, threading


def thread_run(urls):
    print('Current %s is running...' % threading.currentThread().name)
    for url in urls:
        print('%s ---->>> %s' % (threading.currentThread().name, url))
        time.sleep(random.random())
    print('%s ended. 1' % threading.currentThread().name)


print('%s is running...' % threading.currentThread().name)
t1 = threading.Thread(target=thread_run, name="Thread-1", args=(['url_1', 'url_2', 'url_3'],))
t2 = threading.Thread(target=thread_run, name="Thread-2", args=(['url_4', 'url_5', 'url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended. 2' % threading.currentThread().name)


# 第二种方法
class myThread(threading.Thread):
    def __init__(self, name, urls):
        super().__init__(name=name)
        # threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print('Current %s is running...' % threading.currentThread().name)
        for url in self.urls:
            print('%s --->>> %s' % (threading.currentThread().name, url))
            time.sleep(random.random())
        print('%s ended.' % threading.currentThread().name)


print("method 2")
print('%s is running...' % threading.currentThread().name)
t3 = myThread(name='Thread-3', urls=['url-7', 'url-8', 'url-9'])
t4 = myThread(name='Thread-3', urls=['url-10', 'url-11', 'url-12'])
t3.start()
t4.start()
t3.join()
t4.join()
print('%s ended. 3' % threading.currentThread().name)

# 线程同步。RLock 可重入锁 Lock 非可重入锁
mylock = threading.RLock()
num = 0


class myThread2(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()  # 请求锁
            print('%s locked, Number: %d' % (threading.currentThread().name, num))
            if num >= 4:
                mylock.release()
                print('%s released, Number: %d' % (threading.currentThread().name, num))
                break
            num += 1
            print('%s released, Number: %d' % (threading.currentThread().name, num))
            mylock.release()  # 释放锁


thread1 = myThread2('Thread-5')
thread2 = myThread2('Thread-6')
thread1.start()
thread2.start()
