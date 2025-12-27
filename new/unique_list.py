l = [1,2,3,4,5,3,2,1,4,5]
def unique_list(l):
    uninque_list = []

    for i in l:
        if i not in uninque_list:
            uninque_list.append(i)
    return uninque_list

print("The unique list is :", unique_list(l))