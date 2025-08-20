import pandas as pd

# Load CSV file
presidents = pd.read_csv("presidents.csv")

print("Head of dataset:\n", presidents.head())

print("tail of dataset:\n", presidents.tail())

print(presidents['Party'].value_counts())

