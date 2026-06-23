# Problem-2: Write a Python function
# that accepts a hyphen-separated 
# sequence of words as parameter and returns the words in a hyphen-separated sequence after 
# sorting them alphabetically.


def h_fun(f):
    words = f.split('-')
    words.sort()
    return '-'.join(words)
a = "green-red-yellow-black-white"
b = h_fun(a)
print(b)        
