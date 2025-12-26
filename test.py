# from datetime import date

# dob = date.fromisoformat(input("Enter your dob (YYYY-MM-DD): "))

# today = date.today()
# age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# if age >= 18:
#     print(f"You are eligible to vote. You are {age} years old.")
# else:
#     print(f"You are not eligible to vote. You are {age} years old.")


dob = input("Enter your dob (YYYYMMDD): ")
age = (2025 - int(dob[:4]))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")