from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def proc_write(q: Queue, urls: str):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


# 读数据进程执行的的代码
def proc_read(q: Queue):
    print('Process (%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)


if __name__ == '__main__':
    q = Queue()
    proc_write1 = Process(target=proc_write, args=(q, ['url_1', 'url_2', 'url_3']))
    proc_write2 = Process(target=proc_write, args=(q, ['url_4', 'url_5', 'url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程写入
    proc_write1.start()
    proc_write2.start()
    # 启动子进程读取
    proc_reader.start()
    # 等待 写入结束
    proc_write1.join()
    proc_write2.join()
    # 强行终止死循环
    proc_reader.terminate()