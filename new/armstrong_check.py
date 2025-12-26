'''
for eg 153 = 1^3 + 5^3 + 3^3 = 153
'''

num = str(input("Enter a number: "))
length = len(num)
sum = 0

while num.isdigit() == False:
    num = str(input("Invalid input. Please enter a valid number: "))

for i in num:
    sum += int(i) ** length

if sum == int(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
