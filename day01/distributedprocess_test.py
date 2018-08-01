# 分布式进程
"""
创建分布式进程需要六个步骤：
1、建立队列 Queue，用来进行进程间通信。包括 任务队列，结果队列。
在分布式环境下，必须通过 Queuemanager 获得的 Queue 接口来添加任务。
2、把第一步中建立的队列在网络上注册，暴露给其他进程（主机），注册后 获得网络队列，相当于本地队列的映像。
3、建立一个对象（Queuemanager(BaseManager))实例 manager，绑定端口和验证口令。
4、启动3建立的实例，即启动 manager，监管信息通道。
5、通过 manager 获得网络访问的 Queue 对象。
6、创建任务到“本地”队列，自动上传任务到网络队列中，分配给任务进程处理。
"""

import random, time
from queue import Queue
from multiprocessing.managers import BaseManager

# 第一步：建立 task_queue 和 result_queue
task_queue = Queue()
result_queue = Queue()


def re_task_queue():
    return task_queue


def re_result_queue():
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 第二步：将队列注册在网络上，利用 register 方法，callable 参数关联 Queue 对象
    QueueManager.register('get_task_queue', callable=re_task_queue)  # windows 下使用
    QueueManager.register('get_result_queue', callable=re_result_queue)    # windows 下使用
    # QueueManager.register('get_task_queue', callable=lambda : task_queue)  # linux 使用
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)  # linux 使用

    # 第三步：绑定端口，设置验证口令
    manager = QueueManager(address=('192.168.1.203', 8001), authkey=b'test')

    # 第四步：启动管理，监听信息通道
    manager.start()

    # 第五步：通过管理实例的方法获得通过网络访问的 Queue 对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 第六步：添加任务
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 获取返回结果
    print('try get result...')
    for i in range(10):
        print('result is %s' % result.get(timeout=10))

    # 关闭管理
    manager.shutdown()
    print('master exit.')
