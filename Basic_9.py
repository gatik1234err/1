# Input a number; print multiplication table (1–10).

num = int(input("Enter a Number: "))

print(f"Multiplication Table of {num}:")

for i in range(1,11):
    print(num, "x" ,i ,"=", num*i)