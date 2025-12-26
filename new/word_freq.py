# Count word frequency in a sentence.
sen = input("Enter a sentence: ")
words = sen.split() #list of all words in sentence
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)