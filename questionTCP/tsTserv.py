#!/usr/bin/env python

from socket import *
from time import ctime

HOST =''
PORT =21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

menu = """
==========================================
	(b)id number
	(c)lose
	(l)ist
==========================================
"""
opt ={
	'b':bid,
	'c':close,
	'l':lis,
}

def bid():
	pass

while True:
	print "waiting for connection..."
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connection from: ', addr

	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if not data or data=='c':
			break
		tcpCliSock.send('[%s] %s'%(ctime(), data))
		print type(data)

	tcpCliSock.close()

tcpSerSock.close()
