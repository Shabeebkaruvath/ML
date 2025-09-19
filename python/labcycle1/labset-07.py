import numpy as np

size = int(input("enter the size of the metrix"))

print(f"Enter elements for a {size}x{size} matrix A:")

 
A = []
B = []
print("enter the values for 1st array:")
for i in range(size):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
print("enter the values for 2nd array:")
for i in range(size):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

 
print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nA + B:\n", A + B)
print("\nA x B:\n", np.dot(A, B))
print("\nTranspose of A:\n", A.T)
 
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

 