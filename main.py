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
    # server.bind(('172.16.16.168', 50001)) #server ip
    server.bind(('127.0.0.1', 50001))  # test ip
    server.listen()


def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))


if __name__ == '__main__':
    try:
        start_tcp_server()
    except:
        pass
    setting = bytearray(800)  # 帧长度
    setting[0] = 0xaa  # 帧头
    setting[1] = 0x55  # 帧头
    setting[2] = 3  # 帧头
    setting[3] = 32  # 帧头
    setting[14] = 0x1  # 帧类型 1：参数设置 2：状态数据
    setting[15] = 0x1  # 帧方向 1：控制器到显示屏 2：显示屏到控制器
    setting[22] = 0x1  # 实例数据
    setting[23] = 0x1  # 实例数据
    # print_hex(key)
    state = bytearray(800)  # 帧长度
    state[0] = 0xaa  # 帧头
    state[1] = 0x55  # 帧头
    state[2] = 3  # 帧头
    state[3] = 32  # 帧头
    state[14] = 0x2  # 帧类型 1：参数设置 2：状态数据
    state[15] = 0x1  # 帧方向 1：控制器到显示屏 2：显示屏到控制器
    state[22] = 0x1  # 实例数据
    state[23] = 0x1  # 实例数据
    recv_buff = bytearray(800)

    while True:
        conn, addr = server.accept()
        while True:
            conn.send(setting)
            # print_hex(setting)
            conn.send(state)
            # print_hex(state)
            # if not key:
            #     print("Don't has data")
            #     break
            time.sleep(1)
            recv_buff = conn.recv(800)
            if not recv_buff:
                print_hex(recv_buff)
                break


    server.close()
