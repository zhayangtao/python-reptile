from multiprocessing import Pipe, Process
import random
import time, os


def proc_send(pipe: Pipe, urls):
    for url in urls:
        print("Process(%s) send: %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe: Pipe):
    while True:
        print("Process(%s) rev: %s" % (os.getpid(), pipe.recv()))
        time.sleep(random.random())

if __name__ == '__main__':
    pipe = Pipe()
    p1 = Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = Process(target=proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


