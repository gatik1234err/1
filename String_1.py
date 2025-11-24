# Input a string and count vowels, consonants, digits, and spaces.

sen = input("Enter a String: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for char in sen:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digit += 1
    else :
        spaces += 1
        
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("Spaces: ", spaces)