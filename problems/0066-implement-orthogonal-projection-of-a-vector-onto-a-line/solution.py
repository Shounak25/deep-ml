import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v,L=np.array(v),np.array(L)
	L_2=np.dot(L,L)
	v_L=np.dot(v,L)
	return (v_L/L_2) * L
