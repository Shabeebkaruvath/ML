import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('dataset.csv')
    print("✅ Data loaded successfully")
except:
    df = pd.read_csv('dataset.csv', encoding='latin-1')
    print("✅ Data loaded with encoding fix")

# Create scatter plot: Goals vs Caps colored by Confederation
plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
confederations = df['Confederation'].unique()

for i, conf in enumerate(confederations):
    data = df[df['Confederation'] == conf]
    plt.scatter(data['Caps'], data['Goals'], 
               c=colors[i % len(colors)], label=conf, alpha=0.7, s=50)

plt.title('Goals vs International Caps by Confederation', fontsize=14)
plt.xlabel('International Caps (Appearances)')
plt.ylabel('Goals Scored')
plt.legend(title='Confederation')
plt.grid(True, alpha=0.3)
plt.show()

# Show results
print(f"\n📊 Plotted {len(df)} players")
print(f"🌍 Confederations: {list(confederations)}")
print("✅ Scatter plot created successfully!")