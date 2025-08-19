import numpy as np
import matplotlib.pyplot as plt


data = np.random.randn(100) 
plt.hist(data,bins=5)
plt.title("Histogram Example")
plt.show()
