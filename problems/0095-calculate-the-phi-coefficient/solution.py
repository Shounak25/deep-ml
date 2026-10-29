def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	# Your code here
	x_00 , x_01 , x_10 , x_11 = 0,0,0,0
	n=len(x)
	for i in range(n):
		if x[i]==0 and y[i]==0:
			x_00+=1
		elif x[i]==0 and y[i]==1:
			x_01+=1
		elif x[i]==1 and y[i]==0:
			x_10+=1
		else:
			x_11+=1
	try:
		val=((x_00*x_11) - (x_01*x_10))/(((x_00+x_01)*(x_10+x_11)*(x_00+x_10)*(x_01+x_11))**0.5)
		return round(val,4)
	except ZeroDivisionError:
		return 0.0