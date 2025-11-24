number= []
for i in range(10):
    num = int(input(f"Enter a {i+1} number: "))
    number.append(num)

second_largest = number[0]
largest = number[0]

for i in range(1,10):
    if number[i] > largest:
        second_largest = largest
        largest = number[i]
    elif number[i] > second_largest:
        second_largest = number[i]

print(f"Second largest number is {second_largest}")
print(f"Largest number is {largest}")
print(number)