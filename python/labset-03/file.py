file = open("print.txt","w")
file.write("text file created")
file.close()


file = open("print.txt","r")
print(file.read())
file.close()
