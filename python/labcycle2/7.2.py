import pandas as pd

data = pd.read_csv('innovators.csv')

early_innovators = data[data["Year"] < 2000]


for name in early_innovators["Name"]:
    print(name)