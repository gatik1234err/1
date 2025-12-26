l = [1,2,3,4,5,6,7,8,9,0]
k = int(input("Enter the number of rotations: " ))

k = k % len(l)
rotated_list = l[-k:] + l[:-k]
print("The rotated list is :", rotated_list)