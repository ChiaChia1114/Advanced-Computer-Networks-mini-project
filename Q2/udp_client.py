#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time
from unicodedata import numeric

HOST = '127.0.0.1'
PORT = 5406
server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_recv.bind(('127.0.0.1', 5407))
sock_recv.settimeout(0.15)


time_stamp_1 = time.time()
for i in range(1,10001):
    msg = 'Hello ' + str(i)
    outdata = msg.encode("utf-8")

    # 傳送訊息給server
    s.sendto(outdata, server_addr)
    # time.sleep(1)
    while True:
        try:
            indata, addr = sock_recv.recvfrom(32768)
            print('recvfrom ' + str(addr) + ': ' + indata.decode())
            break
        except socket.timeout:
            break
time_stamp_2 = time.time()
latency = time_stamp_2 - time_stamp_1
print('Whole process cost '+ str(latency) + ' s')
