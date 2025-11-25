# Input two sets and print union, intersection, and difference.
s1 = set(input("Enter values : ").split())
s2 = set(input("Enter values : ").split())

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))