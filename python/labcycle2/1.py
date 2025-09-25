lim=int(input("enter the limit:"))

words=[]
index =[]

for i in range(lim):
    word=input("Enter a word:")
    words.append(word)

term=input("enter the the word to search:")

for i, data in enumerate(words):
    if term in data:
        index.append(i)
        words[i]="1"
    else:
       words[i]="0"
   
print("containing word index positions are:")    
print(index)
print("containing word index value changed:")    
print(words)
 
 
