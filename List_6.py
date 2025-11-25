# Find the sum of all elements in a list without using sum().

l = [2,2,2,2,2]
s = 0

for i in l:
    s = s + l[i]
print(s)