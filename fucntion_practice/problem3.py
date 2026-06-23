# ### **`Problem-3:`**
# Write a Python function that accepts a string and calculates
# the number of uppercase letters and lowercase letters.

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

text = "Hello World"
u, l = count_case(text)
print("Uppercase:", u)
print("Lowercase:", l)