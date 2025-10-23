import csv
from datetime import datetime, timedelta
import random

# CSV file name
filename = "monthly_sales.csv"

# Columns
fields = ["Date", "Electronics", "Clothing", "Groceries", "Furniture", "Profit"]

# Generate dates for this month
today = datetime.today()
start_date = today.replace(day=1)
days_in_month = (today.replace(month=today.month % 12 + 1, day=1) - timedelta(days=1)).day

rows = []
for day in range(1, days_in_month + 1):
    date = start_date.replace(day=day).strftime("%Y-%m-%d")
    electronics = random.randint(1000, 5000)
    clothing = random.randint(500, 3000)
    groceries = random.randint(200, 2000)
    furniture = random.randint(800, 4000)
    profit = electronics + clothing + groceries + furniture - random.randint(1000, 3000)  # example
    rows.append([date, electronics, clothing, groceries, furniture, profit])

# Write CSV
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)

print(f"CSV '{filename}' created for this month.")
