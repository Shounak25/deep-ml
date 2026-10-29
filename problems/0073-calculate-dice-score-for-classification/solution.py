
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp,fp,fn=0,0,0
	n=len(y_true)
	for i in range(n):
		if y_pred[i]==1 and y_true[i]==1:
			tp+=1
		if y_pred[i]==1 and y_true[i]==0:
			fp+=1
		if y_pred[i]==0 and y_true[i]==1:
			fn+=1
	if tp==0 and fp==0 and fn==0:
		return 0.0
	res=(2*tp)/(2*tp + fp + fn)	
	return round(res, 3)
