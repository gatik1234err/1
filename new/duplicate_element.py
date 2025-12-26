l = [10,20,40,10,20,30,40,50,30]
d = []
for i in l:
    if i not in d:
        d.append(i)
print("The list after removing duplicate elements is :", d)