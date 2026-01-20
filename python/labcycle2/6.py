import pandas as pd


df = pd.read_csv('6.csv')

df.drop_duplicates(inplace=True)
df.fillna({
    'marks': df['marks'].mean(),
    'grade': 'N/A',
    'subject': 'Unknown',
    'name': 'Unknown'
}, inplace=True)


max_subject = df.loc[df.groupby('subject')['marks'].idxmax()]
max_subject.to_csv('max_subject.csv', index=False)


avg_grade = df.groupby('grade')['marks'].mean().reset_index()
avg_grade.to_csv('avg_grade.csv', index=False)


df.to_csv('cleaned_students.csv', index=False)


print("Cleaned Data:")
print(df.head())
print("\nMax Marks Per Subject:")
print(max_subject)
print("\nAverage Marks Per Grade:")
print(avg_grade)
