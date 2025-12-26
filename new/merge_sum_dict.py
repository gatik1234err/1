d1 = {"a": 1, "h": 2, "c": 3, "d": 4}
d2 = {"a": 10, "b": 20, "c": 30, "f": 40}

for key in d2:
    if key in d1:
        d1[key] = d1[key] + d2[key]
    else:
        d1[key] = d2[key]

print(d1)