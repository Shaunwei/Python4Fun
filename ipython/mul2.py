import numpy
def mul2(n):
	# import ipdb;ipdb.set_trace()
	M = numpy.arange(1,n+1).reshape((-1,1))
	M = numpy.tile(M,(1,n))
	N = numpy.arange(1,n+1).reshape((1,-1))
	N = numpy.tile(N,(n,1))
	return M*N
