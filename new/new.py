import timer
n = int(input("Enter a number: "))
even_number = [num for num in range(1,n) if num%2 == 0]
for i in even_number:
    print(i)
print("Total even numbers are:", len(even_number))