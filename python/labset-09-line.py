import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 50)
print(x)
y = np.sin(x)
print(y)

plt.plot(x, y)
plt.title("Line Graph (Sine Wave)")
plt.show()
 