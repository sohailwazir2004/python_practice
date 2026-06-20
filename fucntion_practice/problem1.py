# ### **`Problem-1:`**
#  Write a Python function that takes a list and returns a
#  new list with unique elements of the first list.

def f_to_list(l):
    return list(set(l))

a = [1,2,3,3,3,3,4,5]
b = f_to_list(a)
print(b)