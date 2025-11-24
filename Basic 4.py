# Input marks of 5 subjects; print total, average, and percentage.

maths = int(input("Enter Maths Marks: "))
english = int(input("Enter English Marks: "))
science = int(input("Enter Science Marks: "))
social = int(input("Enter Social Marks: "))
hindi = int(input("Enter Hindi Marks: "))

total = maths + english + science + social + hindi
average = total / 5
percentage = (total / 500) * 100

print("Total Marks: ", total)
print("Average Marks: ", average)
print("Percentage: ", percentage)