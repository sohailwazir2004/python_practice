# # Problem 4: Write a Python program to print
# # the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]


def even_list(l):
    n_list = []
    for num in l:
        if num%2 == 0:
            n_list.append(num)
    return n_list

l = [1,2,3,4,5,6,7,8,9]
n_list = even_list(l)
print(n_list)