import pandas as pd

 
try:
    df = pd.read_csv('dataset.csv')  
except UnicodeDecodeError:
    df = pd.read_csv('dataset.csv', encoding='latin-1')  
    

print("\n First 5 rows:")
print(df.head())

print("\n Last 5 rows:")
print(df.tail())
 
print("\n Missing values:")
missing = df.isnull().sum()
for col, count in missing.items():
    print(f"{col}: {count}")

 

 
print("\n Goals Statistics:")
print(f"Mean: {df['Goals'].mean():.2f}")
print(f"Median: {df['Goals'].median():.2f}")
mode = df['Goals'].mode()
print(f"Mode: {mode[0] if len(mode) > 0 else 'None'}")

