l = [10,30,20,50,40]
# l.sort()
# print("The second largest number in the list is :", l[-2])

left=0
right=len(l)-1
for i in range(len(l)):
    for j in range(0, right-i):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print("The second largest number in the list is :", l[-2])