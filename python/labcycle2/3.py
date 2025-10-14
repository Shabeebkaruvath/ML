import numpy as np


A = np.array([[1, 1],      # Coefficients of c and a in equation 1
              [1.5, 4]])    # Coefficients of c and a in equation 2

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