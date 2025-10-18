

input_text = input("Text: ")
words = input_text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word = sorted(word_count)

max_length = max(len(word) for word in sorted_word)

for word in sorted_word:
    print(f"{word:{max_length}}: {word_count[word]}")