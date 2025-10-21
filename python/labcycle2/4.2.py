import pandas as pd
import matplotlib.pyplot as plt

# Load the data from your CSV file
data = pd.read_csv('4.2.csv')

# Plot toothpaste sales against month number
plt.scatter(data['month_number'], data['toothpaste'], color='blue')
plt.title('Toothpaste Sales Over Months')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales (Units)')
plt.grid(True)
plt.show()

