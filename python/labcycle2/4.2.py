import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('4.2.csv')

total_sales = data[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].scatter(data['month_number'], data['toothpaste'], color='blue')
axs[0, 0].set_title('Toothpaste Sales')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Sales')

axs[0, 1].bar(data['month_number'] - 0.2, data['facecream'], width=0.4, label='Face Cream', color='green')
axs[0, 1].bar(data['month_number'] + 0.2, data['facewash'], width=0.4, label='Face Wash', color='orange')
axs[0, 1].set_title('Face Cream & Face Wash Sales')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Sales')


axs[1, 0].pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
axs[1, 0].set_title('Total Sales Distribution')

axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
