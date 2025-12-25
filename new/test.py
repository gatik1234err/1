l1 = [1,2,3]
l2 = [4,5,6]

num1 = int()
num2 = int()

for i in range(len(l1)):
    num1 = l1
    num2 = l2[i] + num2

print(num1)
print(num2)