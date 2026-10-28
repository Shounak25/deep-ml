
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	
	n=len(y_true)
	y_mean=np.mean(y_true)
	# print(y_mean)
	ssr,sst=0,0
	for i in range(n):
		ssr+=(y_true[i]-y_pred[i])**2
	for i in range(n):
		sst+=(y_true[i]-y_mean)**2
	return 1 - (ssr/sst)