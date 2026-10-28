import numpy as np
def precision(y_true, y_pred):
	tp,fp=0,0
	n=len(y_true)
	for i in range(n):
		if y_true[i]==1 and y_pred[i]==1:
			tp+=1
		if y_pred[i]==1 and y_true[i]==0:
			fp+=1
	if tp==0 and fp==0:
		return 0
	return tp/(tp+fp)