#!/usr/bin/env python


for x in xrange(1,100):
	if x ==77:
		continue
	x = str(x)
	if len(x)<2:
		x = '0' + x
	filename = 'JCP0' + str(x) +'.py'
	try:
		with open(filename,'rb') as inputf, open('test.py', 'at') as ouputf:
			for line in inputf.readlines():
				try:				
					line = line.decode('GBK').encode('UTF-8')
					ouputf.write(line)
				except UnicodeDecodeError:
					pass
	except IOError,UnicodeDecodeError:
		pass



