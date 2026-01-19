from sklearn.linear_model import Perceptron
from sklearn.feature_extraction.text import CountVectorizer

reviews = [
    "I absolutely loved the plot",
    "The acting was terrible",
    "Highly recommended for everyone",
    "I fell asleep halfway through",
    "A masterpiece of modern cinema",
    "The ending was very disappointing",
    "Brilliant performance by the lead",
    "Save your money and skip this",
    "Such a refreshing and fun story",
    "Poor direction and bad lighting",
    "The tea is good",                 
    "This is a good movie",            
    "The food was bad"                 
]

# Labels (1 for positive, 0 for negative)
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# 3. Apply Perceptron
clf = Perceptron()
clf.fit(X, labels)


new_review = [input("enter a review::")]
new_X = vectorizer.transform(new_review)
prediction = clf.predict(new_X)

print("Sentiment:", "Positive" if prediction[0] == 1 else "Negative")