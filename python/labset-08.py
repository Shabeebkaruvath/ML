import pandas as pd

# Load CSV file with encoding fix
try:
    df = pd.read_csv('dataset.csv')  # Try UTF-8 first
except UnicodeDecodeError:
    df = pd.read_csv('dataset.csv', encoding='latin-1')  # Try latin-1
    

# 2. Display head and tail
print("\n🔝 First 5 rows:")
print(df.head())

print("\n🔚 Last 5 rows:")
print(df.tail())

# 3. Check missing values
print("\n🔍 Missing values:")
missing = df.isnull().sum()
for col, count in missing.items():
    print(f"{col}: {count}")

# 4. Handle missing values if any
if missing.sum() > 0:
    # Fill numbers with median, text with 'Unknown'
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['int64', 'float64']:
                df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna('Unknown', inplace=True)
    print("✅ Missing values fixed!")

# 5. Goals statistics only
print("\n📈 Goals Statistics:")
print(f"Mean: {df['Goals'].mean():.2f}")
print(f"Median: {df['Goals'].median():.2f}")
mode = df['Goals'].mode()
print(f"Mode: {mode[0] if len(mode) > 0 else 'None'}")

