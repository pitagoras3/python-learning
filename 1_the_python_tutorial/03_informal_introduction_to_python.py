# Comments start with character

text = "# Hash character inside the string does not start a comment"

print(10 / 5)  # 2.0 - division always returns a floating point number
print(11 // 5)  # 2 - // floor division operator
print(11 % 5)  # 1 - remainder of the dividion
print(2**10)  # 1024 - 2 to the power of 10

name = "Szymon"
surname = "Marcinkiewicz"
print(name + " " + surname)  # Szymon Marcinkiewicz
# print(age) # NameError: name 'age' is not defined

print("Double quotes string")  # Double quotes string
print('Single quotes string')  # Single quotes string

# Using single quotes 'in double quotes'
print("Using single quotes 'in double quotes'")

# Using double quotes "in single quotes"
print('Using double quotes "in single quotes"')

print("escaping double quote \"")  # escaping double quote "
print('escaping single quote \'')  # escaping single quote '

# escaping single quote inside double quote is not needed '
print("escaping single quote inside double quote is not needed \'")

# escaping single quote inside double quote is not needed '
print("escaping single quote inside double quote is not needed '")

print("\backslash\path")  # ackslash\path
print(r"\backslash\path")  # \backslash\path - raw strings
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  # Multiline string. Backslash after """ prevents empty new line

print("ma" * 2)  # mama
broken_string = (
    'broken '
    'string'
)
print(broken_string)  # broken string
print(
    'multiline '
    'broken '
    'string'
)  # multiline broken string
string_concatenation = 'String concatenation ' + "works perfectly " + 'normally.'
print(string_concatenation)  # String concatenation works perfectly normally.
print("Character"[0])  # C - Character -> [C]haracter
print("Character"[0][0])  # C - Character -> [C]haracter -> [C]

# C - Character -> [C]haracter -> [C] -> [C] - there is no "Char" type, Char is String of length 1
print("Character"[0][0][0])

print("ABCDE"[-1])  # E - [-1] prints last character
# print("ABCDE"[0.6])  # TypeError: string indices must be integers

# 123 - characters from position 1 (included) to 4 (excluded)
print("012345"[1:4])

print("012345"[:4])  # 0123 - an omitted first index defaults to zero

# 2345 - an omitted second index defaults to the size of the string being sliced
print("012345"[2:])

test_numbers = "012345678"
print(test_numbers[:-2] + test_numbers[-2:])  # 012345678

# One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0.
# Then the right edge of the last character of a string of n characters has index n, for example:

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

# test_numbers[2] = 3  # TypeError: 'str' object does not support item assignment

# 013345678 - as Python strings are immutable if we want to change it, we have to create a new one
print(test_numbers[:2] + "3" + test_numbers[3:])

print(len(test_numbers))  # 9 - len function returns length of the string
test_list = [1, "2", 3.0, '4']  # lists can contain multiple datatypes at once :(

# slice made from the beginning to the end of the test_list creates shallow copy of the test_list - https://docs.python.org/3/library/copy.html#shallow-vs-deep-copy
shallow_copy_list = test_list[:]

concatenated_list = test_list + [5, 6, 7, 8]
concatenated_list[2] = 2  # lists are mutable (not like immutable strings)
# print(concatenated_list + 9)  # TypeError: can only concatenate test_list (not "int") to test_list
print(concatenated_list + [9])  # [1, '2', 2, '4', 5, 6, 7, 8, 9]

# [1, '2', 2, '4', 5, 6, 7, 8] (concatenation in the line above added the new element only temporarily)
print(concatenated_list)

concatenated_list.append(9)

# [1, '2', 2, '4', 5, 6, 7, 8, 9] (append in the line above added the new element permanently)
print(concatenated_list)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
letters[2:6] = ["C", "D", "E", "F"]
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'F', 'g', 'h']
letters[2:6] = []
print(letters)  # ['a', 'b', 'g', 'h']
letters[:] = []  # Clear whole test_list
# clear the test_list by replacing all the elements with an empty test_list
print(letters)
len(letters)  # 0

child1 = [1, 2, 3]
child2 = ['a', 'b', 'c']
parent = [child1, child2]
print(parent)  # [[1, 2, 3], ['a', 'b', 'c']]
print(parent[0])  # [1, 2, 3]
print(parent[0][1])  # 2


def fibonacci(n):
    counter = 0
    a, b = 0, 1  # multiple assignement
    while (counter < n):
        # print function takes multiple arguments, formats elements with space between them
        print(counter, ":", a)
        a, b = b, a+b
        counter += 1


fibonacci(10)


def fibonacci_rec(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


print(fibonacci_rec(8), fibonacci_rec(9), sep="_", end=":)\n")  # 21_34:)
