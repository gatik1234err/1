# Count how many times each item appears in a list.

l = [1,2,3,1,3,5,6,3]
d = {}

for i in l: 
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
print(d)