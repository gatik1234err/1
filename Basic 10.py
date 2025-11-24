a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))

if a > b and a > c:
    print(f"{a} is the largest number")
elif b > a and b > c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")