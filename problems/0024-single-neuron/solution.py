import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	z=np.dot(features,weights) + bias
	probabilities = [1/(1+math.exp(-x)) for x in z]
	mse=0
	n=len(probabilities)
	for i in range(n):
		mse+=(labels[i]-probabilities[i])**2
	mse=mse/n
	return probabilities, mse