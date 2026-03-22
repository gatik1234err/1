# with open('example.txt', 'r') as f:
#     for line in f:
#         words = line.split()
#         freq = {}
#         for word in words:
#             word = word.strip('.,!?";:()[]').lower()
#             if word in freq:
#                 freq[word] += 1
#             else:
#                 freq[word] = 1
#     print("Most frequent word in line:", max(freq, key=freq.get))


import collections
with open('example.txt', 'r') as f:
    for line in f:
        words = line.split()
        freq = {}
        for word in words:
            word = word.strip('.,!?";:()[]').lower()
            count = collections.Counter(words)
            freq.update(count)
    print("Most frequent word in line:", max(freq, key=freq.get), "appeared", freq[max(freq, key=freq.get)], "times")
