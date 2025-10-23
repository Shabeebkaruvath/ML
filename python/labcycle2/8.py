import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('8.csv')

 
month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)

 
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.delaxes(axes[1,1]) 
 
axes[0,0].plot(df['month'], df['profit'], marker='o', color='b')
axes[0,0].set_title('Monthly Profit Trend')
axes[0,0].set_xlabel('Month')
axes[0,0].set_ylabel('Profit')
axes[0,0].grid(True)

 
df_monthly = df.set_index('month')[['electronics', 'clothing']]
df_monthly.plot(kind='bar', ax=axes[0,1])
axes[0,1].set_title('Electronics and Clothing Sales')
axes[0,1].set_xlabel('Month')
axes[0,1].set_ylabel('Sales')

 
df_total = df[['electronics', 'clothing', 'groceries', 'furniture']].sum()
axes[1,0].pie(df_total, labels=df_total.index, autopct='%1.1f%%', startangle=90)
axes[1,0].set_title('Total Yearly Sales by Category')

plt.tight_layout()
plt.show()
