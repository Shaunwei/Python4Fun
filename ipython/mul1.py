import numpy
def mul1(n):
	return numpy.array([[(i+1)*(j+1) for i in xrange(n)] for j in xrange(n)])

	