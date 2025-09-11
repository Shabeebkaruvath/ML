import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('dataset.csv')
except:
    df = pd.read_csv('dataset.csv', encoding='latin-1')

plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
confederations = df['Confederation'].unique()

for i, conf in enumerate(confederations):
    data = df[df['Confederation'] == conf]
    plt.scatter(data['Caps'], data['Goals'], 
               c=colors[i % len(colors)], label=conf, alpha=0.7, s=50)

plt.title('Goals vs International Caps by Confederation', fontsize=14)
plt.ylabel('Goals Scored')
plt.legend(title='Confederation')
plt.grid(True, alpha=0.3)
plt.show()
 