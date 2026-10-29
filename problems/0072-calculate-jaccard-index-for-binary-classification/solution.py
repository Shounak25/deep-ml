
import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
	n=len(y_true)
	a,b=0,0
	for i in range(n):
		if y_true[i]==1 and y_pred[i]==1:
			a+=1
		if y_true[i]==1 or y_pred[i]==1:
			b+=1
	result=a/b
	return round(result, 3)
