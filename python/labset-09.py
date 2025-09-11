import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
try:
    df = pd.read_csv('dataset.csv')
except:
    df = pd.read_csv('dataset.csv', encoding='latin-1')

# Create plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

# 1. Line plot: y = x²
x = np.linspace(-5, 5, 50)
ax1.plot(x, x**2, 'b-')
ax1.set_title('y = x²')

# 2. Bar chart: Top 5 scorers
top5 = df.head(5)
ax2.bar(range(5), top5['Goals'])
ax2.set_title('Top 5 Goal Scorers')
ax2.set_xticks(range(5))
ax2.set_xticklabels([name.split()[-1] for name in top5['Player']])

# 3. Bar chart: Goals by confederation
conf_goals = df.groupby('Confederation')['Goals'].sum()
ax3.bar(conf_goals.index, conf_goals.values)
ax3.set_title('Goals by Confederation')

# 4. Histogram: Goals distribution
ax4.hist(df['Goals'], bins=10, alpha=0.7)
ax4.set_title('Goals Distribution')

plt.tight_layout()
plt.show()