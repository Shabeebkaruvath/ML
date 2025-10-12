import numpy as np

# Linear Equations:
# c + a = 2200        (Equation 1)
# 1.5c + 4a = 5050    (Equation 2)

# Coefficient matrix A (left side of equations)
A = np.array([[1, 1],      # Coefficients of c and a in equation 1
              [1.5, 4]])    # Coefficients of c and a in equation 2

# Constants matrix b (right side of equations)
b = np.array([2200, 5050])

# Solve using np.linalg.solve()
solution = np.linalg.solve(A, b)

children = solution[0]
adults = solution[1]

print("Solution:")
print(f"Number of children: {int(children)}")
print(f"Number of adults: {int(adults)}")

# Verification
print("\nVerification:")
print(f"Total people: {int(children + adults)}")
print(f"Total money: Rs {1.5 * children + 4 * adults}")