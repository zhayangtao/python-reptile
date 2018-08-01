"""
创建和运行 TCP 服务端一般需要五个步骤
1、创建 socket，绑定 socket 到本地 Ip 与端口
2、监听连接
3、循环接受客户端连接请求
4、接受数据，发送数据
5、关闭 socket
"""

import socket
import threading
import time


def dealClient(sock: socket.socket, addr):
    # 第四步：接受数据，发送数据
    print('Accept new connection from %s: %s...' % addr)
    sock.send(b'hello world')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('---> %s!' % data.decode('utf-8'))
        sock.send(('Loop_Msg: %s!' % data.decode('utf-8')).encode('utf-8'))


if __name__ == '__main__':
    # 第一步：创建 socket，基于 ipv4 和 TCP 协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    # 第二步：监听
    s.listen(5)
    print('Waiting for connection...')
    while True:
        # 第三步：接受连接
        sock, addr = s.accept()
        # 创建新线程处理 TCP 连接
        t = threading.Thread(target=dealClient, args=(sock, addr))
        t.start()
