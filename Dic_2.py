# Create a dictionary of 5 students marks and print topper.
marks = {"Rahul": 80, "Sumit": 90, "Sagar": 70, "Raman": 60, "Karan": 95}

Doogla = max(marks, key=marks.get)
print(f"The topper is {Doogla} with marks {marks[Doogla]}")

