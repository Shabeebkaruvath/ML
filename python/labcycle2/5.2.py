def word_positions_in_sentences():
    num_sentences = int(input("Enter the number of sentences: "))
    sentences = []
    for i in range(num_sentences):
        sentence = input(f"Enter sentence {i + 1}: ")
        sentences.append(sentence)
    
    target_word = input("Enter the target word: ")

    result = {i: (s.split().index(target_word) if target_word in s.split() else -1)
              for i, s in enumerate(sentences)}

    print("Word positions in sentences:", result)

# Call the function
word_positions_in_sentences()
