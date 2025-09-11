import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

 
try:
    df = pd.read_csv('dataset.csv')
except:
    df = pd.read_csv('dataset.csv', encoding='latin-1')

 
fig, ((ax1, ax2, ax4)) = plt.subplots(1, 3, figsize=(9, 6))

 
x = np.linspace(-10, 10, 50)
ax1.plot(x, x**2, 'b-')
ax1.set_title('y = x²')

 
top5 = df.head(5)
ax2.bar(range(5), top5['Goals'])
ax2.set_title('Top 5 Goal Scorers')
ax2.set_xticks(range(5))
ax2.set_xticklabels([name.split()[-1] for name in top5['Player']])

 
ax4.hist(df['Goals'], bins=5, alpha=0.4)
ax4.set_title('Goals Distribution')

plt.tight_layout()
plt.show()