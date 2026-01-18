import numpy as np
import pandas as pd
from sklearn import svm

 
def word_to_coords(word):
    return [ord(word[0].lower()) - 96, ord(word[1].lower()) - 96]

 
training_words = ['is', 'it', 'he', 'as', 'to', 'in', 'qc', 'qx', 'zj', 'zp', 'xk', 'vf']
X = [word_to_coords(w) for w in training_words]
y = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]  

# 3. Design the SVM
# We use a 'rbf' (Non-linear) kernel because language patterns are complex
clf = svm.SVC(kernel='rbf', C=1.0)
clf.fit(X, y)

# 4. Test it!

test_word = input("enter a word ::")# Change this to "qc" to see the difference
test_coords = [word_to_coords(test_word)]
prediction = clf.predict(test_coords)

result = "realword" if prediction[0] == 1 else "gibberish"
print(f"The word '{test_word}' is classified as: {result}")