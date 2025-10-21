import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('4.2.csv')

total_sales = data[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

fig, axs = plt.subplots(2, 2, figsize=(14, 10))  

axs[0, 0].scatter(data['month_number'], data['toothpaste'], color='blue')
axs[0, 0].set_title('Toothpaste Sales Over Months')
axs[0, 0].set_xlabel('Month Number')
axs[0, 0].set_ylabel('Toothpaste Sales (Units)')
axs[0, 0].grid(True)


bar_width = 0.4
months = data['month_number']
axs[0, 1].bar(months - bar_width/2, data['facecream'], width=bar_width, label='Face Cream', color='skyblue')
axs[0, 1].bar(months + bar_width/2, data['facewash'], width=bar_width, label='Face Wash', color='orange')
axs[0, 1].set_title('Face Cream and Face Wash Sales Over Months')
axs[0, 1].set_xlabel('Month Number')
axs[0, 1].set_ylabel('Sales (Units)')
axs[0, 1].legend()
axs[0, 1].grid(True)


axs[1, 0].pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
axs[1, 0].set_title('Total Sales Distribution by Product (Last Year)')
axs[1, 0].axis('equal')  

axs[1, 1].axis('off')

plt.tight_layout()
plt.show()
