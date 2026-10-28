import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1_v2=np.dot(v1,v2)
	v1_2=np.dot(v1,v1)
	v2_2=np.dot(v2,v2)
	return v1_v2 / (((v1_2)**0.5) * ((v2_2)**0.5))