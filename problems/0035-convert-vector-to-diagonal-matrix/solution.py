import numpy as np

def make_diagonal(x):
	n=len(x)
	arr=np.zeros((n,n))
	for i in range(n):
		arr[i][i]=x[i]
	return arr