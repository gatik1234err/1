# Convert a list to tuple and tuple back to list.

l = [1,2,3,1,3,5,6,3]
t = tuple(l)
print(t,type(t))

l1 = list(t)
print(l1,type(l1))
