import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	n,d=len(X),len(X[0])
	temp=np.dot(X,w)
	sum1=0
	for i in range(n):
		sum1+=(y_true[i]-temp[i])**2
	sum1=sum1/n
	sum2=0
	for i in range(d):
		sum2+=(w[i])**2
	sum2*=alpha
	return sum1+sum2
