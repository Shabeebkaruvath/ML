fruits = [
    'Apple', 'Banana', 'Orange', 'Mango','Strawberry', 'Grapes',
    'Strawberry', 'Watermelon', 'Orange','Pineapple','Strawberry', 'Papaya', 'Kiwi','Orange'
]

for i in range(len(fruits)):
    fruits[i] = fruits[i].lower()

word= input("Enter the fruit name: ")
count = fruits.count(word.lower())
print(f"{word} : {count} times ")