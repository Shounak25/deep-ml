import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	Max=max(scores)
	n=len(scores)
	result=np.zeros(n)
	total=0
	for j in range(n):
		total+=np.exp(scores[j]-Max)
	for i in range(n):
		result[i]=scores[i] - Max - np.log(total)
	return result