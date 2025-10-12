import pandas as pnd

data = pnd.read_csv('auto.csv')

 
for col in data.columns:
    if data[col].isnull().any():
        if data[col].dtype in ['float64', 'int64']:
            data[col].fillna(data[col].mean(), inplace=True)
data.to_csv('auto_cleaned.csv', index=False)
print("CSV cleaned and saved!\n")

 
data['company'] = data['car name'].str.split().str[0]
print("Total Cars by Company:")
print(data['company'].value_counts())

 
print("\nAverage MPG (Mileage) by Company:")
print(data.groupby('company')['mpg'].mean().sort_values(ascending=False))