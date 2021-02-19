from scipy import linalg
import numpy as np

#Ex a
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Ex a')
print(mat)
print('\n')

#Ex b
vec = np.array([1,2,3])
print('Ex b')
print(vec)
print('\n')

#Ex c
solve = linalg.solve(mat,vec)
print('Ex b')
print(solve)
print('\n')

#Ex d
check = np.matmul(mat,solve)
print('Ex d')
print(check,vec)
print('\n')

#Ex e
mat = np.array([[1,0,0],[0,2,0],[0,0,3]])
B = np.random.random((3,3))
solve_B = linalg.solve(mat,B)
check_B = np.matmul(mat,solve_B) 
print('Ex e')
print('Solve: ',solve_B)
print('Check solve: ',check_B)
print('B :',B)
print('\n')

#Ex f
mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = np.array([[1,0,0],[0,2,0],[0,0,3]])
print('Ex f')
print('Eigenvalues')
print(linalg.eig(mat1)[0])
print(linalg.eig(mat2)[0])
print('Eigenvectors')
print(linalg.eig(mat1)[1])
print(linalg.eig(mat2)[1])
print('\n')

#Ex g
inv1 = linalg.inv(mat1)
inv2 = linalg.inv(mat2)
det1 = linalg.det(mat1)
det2 = linalg.det(mat2)
print('Ex g')
print('Inverse')
print(inv1)
print(inv2)
print('Determinant')
print(det1)
print(det2)
print('\n')

#Ex h
norm_fro = linalg.norm(mat1,ord='fro')
norm_1 = linalg.norm(mat1,ord=1)
norm_2 = linalg.norm(mat1,ord=2)
#norm_3 = linalg.norm(mat1,ord=3)
#norm_4 = linalg.norm(mat1,ord=4)
#norm_5 = linalg.norm(mat1,ord=5)
#norm_6 = linalg.norm(mat1,ord=6)
print('Ex h')
print('Fro norm: ',norm_fro)
print('Order 1 norm: ',norm_1)
print('Order 2 norm: ',norm_2)
#print('Order 3 norm: ',norm_3)
#print('Order 4 norm: ',norm_4)
#print('Order 5 norm: ',norm_5)
#print('Order 6 norm: ',norm_6)
print('\n')
