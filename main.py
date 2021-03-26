"""
This is a testing program
the program is used to start server
"""
import socket
import time
from http import server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.socket()


def start_tcp_server():
    server.bind(('172.16.16.168', 50001)) #server ip
    # server.bind(('127.0.0.1', 50001)) #test ip
    server.listen()


def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))


if __name__ == '__main__':
    try:
        start_tcp_server()
    except:
        pass
    key = bytearray(100) #帧长度
    key[0] = 0xaa  # 帧头
    key[1] = 0x55  # 帧头
    key[14] = 0x1  # 帧类型 1：参数设置 2：状态数据
    key[15] = 0x1  # 帧方向 1：控制器到显示屏 2：显示屏到控制器
    key[22] = 0x1  # 实例数据
    key[23] = 0x1  # 实例数据
    print_hex(key)

    while True:
        conn, addr = server.accept()
        while True:
            print_hex(key)
            if not key:
                print("Don't has data")
                break
            time.sleep(2)
            conn.send(key)
    server.close()
