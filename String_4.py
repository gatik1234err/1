# Print characters at even index positions.

string = input("Enter a String: ")

for i in range(0, len(string), 2):
    print(string[i])