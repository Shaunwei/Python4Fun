#!/usr/bin/env python

from socket import *
from time import ctime

HOST =''
PORT =21577
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

itemBidList={
				'itemName': [0, '1', '2'], #example
			} #itemName, minBid, maxBid

itemIndex =['itemName',]			#example #itemId, itemName 


menu = """
==========================================
	(b)id itemId bidingPrice
	(p)ost itemName minBid
	(l)ist
==========================================
"""
# opt ={
# 	'b':bid,
# 	'p':post,
# 	'l':lis,
# }

def post(itemName, minBid):
	if itemName in itemBidList:
		return 0
	else:
		maxBid = 0
		itemIndex.append(itemName)
		ind = itemIndex.index(itemName)
		itemBidList[itemName] = [ind, minBid,maxBid]
		return '#Current itemIndex: %i' %ind


def bid(itemId, bidingPrice):
	if len(itemIndex)-1 < itemId:
		return 'There are no such id'
	else:
		bidlis = itemBidList[itemIndex[itemId]]
		if bidingPrice< int(bidlis[1]):
			return 'Need to be larger than min bid price => %s' %bidlis[1]
		elif bidingPrice >int(bidlis[2]):
			bidlis[2] = str(bidingPrice)
			return 'You bid is the current highest'
		else:
			return 0

def lis():
	for i in itemBidList.iteritems():
		print "#itemId:%i;   #itemName:%s;   #minBid:%s;   #maxBid:%s; " %(i[1][0], i[0], i[1][1],i[1][2])
	

def main():
	try:
		while True:
			print "waiting for connection..."
			tcpCliSock, addr = tcpSerSock.accept()
			print '...connection from: ', addr

			while True:
				print menu
				data = tcpCliSock.recv(BUFSIZ)
				arg = data.split(' ')
				res =''
				if not data or arg[0]=='c':
					break
				elif arg[0] =='l':
					lis()
				elif arg[0] =='p':
					print 'posting data...'
					res = post(arg[1],arg[2])
					print res
				elif arg[0] =='b':
					res = bid(int(arg[1]),int(arg[2]))
					print res


				tcpCliSock.send('[%s] %s >response:%s'%(ctime(), data, res))
				print 'Your command:',data

			tcpCliSock.close()
	except KeyboardInterrupt:
		print "server closed...", ADDR
		tcpSerSock.close()


if __name__ == '__main__':
	main()