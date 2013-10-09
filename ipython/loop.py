def closest(positon, positons):
	x0, y0 = positon
	dbest, ibest = None, None
	for i, (x,y) in enumerate(positons):
		# squared Euclidean distance from every positon to the positon of interest
		d = (x - x0) **2 + ( y - y0) **2
		if dbest is None or d<dbest:
			dbest , ibest = d,i
	return ibest
	