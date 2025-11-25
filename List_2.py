l = [1,2,3,1,3,5,6,3]
u = []

for i in l:
    if i not in u:
        u.append(i)
print(u)