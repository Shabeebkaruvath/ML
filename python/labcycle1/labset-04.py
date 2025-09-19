class Data:
    name = ""
    age = 22

n = int(input("How many user data you want to store:"))

Datas = []

while n != 0:
    p1 = Data()
    p1.name = input("enter name:")
    p1.age = int(input("enter age:"))
    Datas.append(p1)
    n -= 1

for i, data in enumerate(Datas,1):
    print(f"\n No:{i} \n Name:{data.name} \n Age:{data.age} \n")
