"""
分布式进程任务进程，创建任务进程的四个步骤：
1、使用 QueueManager 注册用于获取 Queue 的方法名称，任务进程只能通过名称在网络上获取 Queue
2、连接服务器，端口和验证口令需要与服务进程一致
3、从网络上获取 Queue，进行本地化
4、从 task 队列获取任务，并写入 result 队列
"""

import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 第一步：使用 QueueManager 注册用于获取 Queue 的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步：连接服务器
server_addr = '192.168.1.203'
print('Connect to server %s...' % server_addr)
manager = QueueManager(address=(server_addr, 8001), authkey=b'test')
manager.connect()

# 第三步：获取 Queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第四步：从 task 获取任务，写入 result 队列
while not task.empty():
    n = task.get(True, timeout=5)
    print('run task')
    time.sleep(1)
    result.put('%s ---> success' % n)

# 处理结束
print('worker exit.')
