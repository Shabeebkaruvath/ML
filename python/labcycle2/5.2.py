def word_positions_in_sentences():
    num_sentences = int(input("Number of sentences: "))
    sentences = []
    for i in range(num_sentences):
        sentence = input(f"Enter sentence {i+1}: ")
        sentences.append(sentence)

    word = input("Enter target word: ")

    result = {}
    for i, sentence in enumerate(sentences):
        words = sentence.split()
        result[i] = words.index(word) if word in words else -1

    return result

positions = word_positions_in_sentences()
print("Word positions in sentences:", positions)
