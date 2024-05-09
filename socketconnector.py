#!/bin/python3

import socket

data = 'Hello world'
ip = '192.168.1.103'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(data.encode())
s.close()
print("Connection successful")
