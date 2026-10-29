import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	n=len(dense_matrix)
	m=len(dense_matrix[0])

	values,Column,Row=[],[],[0]
	count=0
	for i in range(n):
		for j in range(m):
			if dense_matrix[i][j]!=0:
				Column.append(j)
				values.append(dense_matrix[i][j])
				count+=1
		Row.append(count)
	
	return (values,Column,Row)