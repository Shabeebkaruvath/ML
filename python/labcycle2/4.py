import pandas as pnd

data=[
    {'SN':1, 'Name':'Linus Torvalds', 'Country':'Finland', 'Contribution':'Linux Kernel', 'Year':1991},
    {'SN':2, 'Name':'Tim Berners-Lee', 'Country':'England', 'Contribution':'World Wide Web', 'Year':1990},
    {'SN':3, 'Name':'Guido van Rossum', 'Country':'Netherlands', 'Contribution':'Python', 'Year':1991}
]
dataframe = pnd.DataFrame(data)

dataframe.to_csv('4.csv', index=False)
print("CSV created\n")