"""
TCP 客户端的创建和运行需要三个步骤
1、创建 socket，连接远程地址
2、发送数据，接受数据
3、关闭socket
"""

import socket


s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print('--->' + s.recv(1024).decode('utf-8'))
s.send(b'hello I am a client')
print('--->' + s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()