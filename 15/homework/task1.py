print("Enter 2 sentences")
first_sentence = input()
second_sentence = input().split(" ")
similar_words = []

for word in first_sentence.split(" "):
    if word in second_sentence:
        similar_words.append(f'"{word}"')


print(f'Similar words are: {", ".join(similar_words)}')
