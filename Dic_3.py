# Word frequency counter from a paragraph (use dict).
para = input("Enter a paragraph: ").lower().split()
d = {}

for word in para:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)