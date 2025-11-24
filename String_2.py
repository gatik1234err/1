string= str(input("Enter a string: "))
string_rev=string[::-1]
if string_rev==string:
    print("Palindrome")
else:
    print("Not Palindrome")