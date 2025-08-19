import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

 
iris = load_iris()

X = iris.data  
 
y = iris.target  

plt.scatter(X[y==0, 0], X[y==0, 2], color="red", label="Setosa")
plt.scatter(X[y==1, 0], X[y==1, 2], color="green", label="Versicolor")
plt.scatter(X[y==2, 0], X[y==2, 2], color="blue", label="Virginica")

plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Iris Dataset - Scatter Plot")
plt.legend()
plt.show()
