import numpy as np

 
size = 2
print(f"Enter elements for a {size}x{size} matrix A:")

 
A = []
for i in range(size):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)

 
B = np.array([[2, 0], [1, 2]])

 
print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
 
print("\nA + B:\n", A + B)

 
print("\nA x B:\n", np.dot(A, B))

 
print("\nTranspose of A:\n", A.T)
 
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

 