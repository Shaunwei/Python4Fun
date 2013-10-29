#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET , SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print "waiting for connection..."
        tcpCliSock, addr = tcpSerSock.accept()
        print "...connected from", addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            print 'The input data is', data
            tcpCliSock.send('[%s] %s' %(ctime(), data))
            
        tcpCliSock.close()
except KeyboardInterrupt:
    pass

finally:
    tcpSerSock.close()
