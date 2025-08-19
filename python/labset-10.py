import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
 
iris = load_iris()
X = iris.data      
y = iris.target    

 
plt.scatter(X[:, 0], X[:, 2], c=y)   

 
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Iris Dataset - Scatter Plot")

plt.show()
