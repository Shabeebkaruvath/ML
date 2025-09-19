lim=int(input("enter the limit:"))

words=[]
index =[]

for i in range(lim):
    word=input("Enter a word:")
    words.append(word)

word=input("enter the the word to search:")

for i, data in enumerate(words,start=1):
    if word in data:
        index.append(i+1)
        words[i]="1"
    else:
       words[i]="0"
   
print("containing word index positions are:")    
print(index)
print("containing word index value changed:")    
print(words)
 
 
lim = int(input("Enter the limit: "))

words = []
index = []

# Collect words
for i in range(lim):
    word = input("Enter a word: ")
    words.append(word)

# Word to search for
word_to_find = input("Enter the word to search for: ")

# Iterate and find indices of words containing the substring
for i, data in enumerate(words):
    if word_to_find in data:
        index.append(i + 1)  # Append 1-based index
        words[i] = "1"       # Change the word to "1"
    else:
        words[i] = "0"       # Change the word to "0"

# Print results
print("Containing word index positions are:")
print(index)

print("Containing word index values changed:")
print(words)
