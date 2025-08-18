limit = int(input("enter a limit : "))
 
for i in range(limit):
    age = int(input("enter your age : "))
    if(age>18):
        print("you are eligible")
        i=+1
    else:
        print("you are not eligible")
        i=+1