# Find the index of a value in a tuple (handle value not present). simple logic 
t = (10, 20, 60, 70, 30, 40, 50, 80)
f = 30

try:
    index = t.index(f)
    print(f"The value {f} is at index {index}")
except ValueError:
    print(f"The value {f} is not present in the tuple")