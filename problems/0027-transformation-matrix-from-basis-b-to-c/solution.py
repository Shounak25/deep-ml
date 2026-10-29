import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	# b=np.array(B)
	# c=np.array(C)

	p=np.dot(np.linalg.inv(C),B)
	n=len(p)

	return p.tolist()