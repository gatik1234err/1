# if __name__ == '__main__':
#     lst = []
#     n = int(input())
    
#     for _ in range(n):
#         command = input().split()
        
#         if command[0] == "insert":
#             lst.insert(int(command[1]), int(command[2]))
#         elif command[0] == "print":
#             print(lst)
#         elif command[0] == "remove":
#             lst.remove(int(command[1]))
#         elif command[0] == "append":
#             lst.append(int(command[1]))
#         elif command[0] == "sort":
#             lst.sort()
#         elif command[0] == "pop":
#             lst.pop()
#         elif command[0] == "reverse":
#             lst.reverse()


# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     t = tuple(integer_list)
#     print(hash(t))


# def swap_case(s):
#     for char in s:
#         if char is char.lower():
#             s = s.replace(char, char.upper())
        
#         if char is char.upper():
#             s = s.replace(char, char.lower())



#     return s


# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# a = "hello world!"
# b = a.c()
# b = a.capitalize()
# print(b)

# def print_rangoli(size):
#     import string
    
#     alphabets = string.ascii_lowercase
#     width = 4 * size - 3
#     lines = []

#     for i in range(size):
#         left = alphabets[size-1:i:-1]
#         right = alphabets[i:size]
#         row = "-".join(left + right)
#         lines.append(row.center(width, "-"))

#     print("\n".join(lines + lines[-2::-1]))



if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


