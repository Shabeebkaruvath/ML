import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
D = A + B
print("\nA + B:\n", D)  

# Matrix multiplication
C = np.dot(A, B)  
print("\nA x B:\n", C)

# Transpose
print("\nTranspose of A:\n", A.T)

# Determinant
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)


if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
else:
    print("\nMatrix A is singular, no inverse exists.")
