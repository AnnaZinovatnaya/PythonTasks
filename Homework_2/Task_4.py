s = "The quick brown fox jumps over the lazy dog"

reversed_words = []
for word in s.split():
    reversed_words.append(word[::-1])
print(" ".join(reversed_words))
