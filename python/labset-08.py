import pandas as pd

# Load CSV file
presidents = pd.read_csv("presidents.csv")

print("Head of dataset:\n", presidents.head(3))

print("tail of dataset:\n", presidents.tail(3))


print("\n\n Average of a president served in days:",presidents['Days_Served'].mean())

 
print("\n\n",presidents['Party'].value_counts())

