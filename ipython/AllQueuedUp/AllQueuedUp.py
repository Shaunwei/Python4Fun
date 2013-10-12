#!/usr/bin/python
from collections import deque
from sys import argv


deq = deque()

def allqueuedup(filename):
	with open(filename) as f:
		for line in f.readlines():
			group = line.rstrip().split(' ')
			command, name =group[0],group[-1]
			control(command,name)


def control(command,name):
	if command =='add':
		deq.append(name)
	elif command =='remove':
		deq.remove(name)
	else:
		print deq.popleft()


# Slower than the top one
# def control(command,name):
# 	res = {
# 		'add'   : lambda x:deq.append(x),
# 		'remove': lambda x:deq.remove(x),
# 		'next'  : lambda x:deq.popleft()
# 	}[command](name) 
# 	if res is not None:
# 		print res

	


if __name__ == '__main__':
	allqueuedup(argv[1])