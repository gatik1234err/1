line_count = 0
word_count = 0
char_count = 0

with open('example.txt', 'r') as f:
    for line in f:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print(f'Lines: {line_count}\nWords: {word_count}\nCharacters: {char_count}')