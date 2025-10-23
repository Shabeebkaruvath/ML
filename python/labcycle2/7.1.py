import pandas as pd

data = [
    [1, "Geoffrey Hinton", "Canada", "Deep Learning", 1986],
    [2, "Yann LeCun", "France", "Convolutional Neural Nets", 1989],
    [3, "Andrew Ng", "USA", "Online ML Courses", 2011],
    [4, "Phila Suoni", "UK", "Artificial Intelligence", 2023],
    [5, "Yemehi Yathi", "France", "Data Analytics", 2025]
]

df = pd.DataFrame(data, columns=["SN", "Name", "Country", "Innovation", "Year"])

df.to_csv("innovators.csv", index=False)

