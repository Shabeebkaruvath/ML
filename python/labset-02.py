#by using non-recursion method
num=int(input("enter the number"))
fact=1
while(num!=0):
    fact=fact*num
    num-=1

print("factorial :"+str(fact))




#by using recursion method
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

num = int(input("enter the number: "))
print("factorial :" + str(fact(num)))
