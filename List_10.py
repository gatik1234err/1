# Find the sum of all elements in a list without using sum().

l = [2,2,2,2,2]
m = 1

for i in l:
    m = m * l[i]
print(m)