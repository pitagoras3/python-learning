from enum import Enum
from typing import List

# x = int(input("Please input a number: "))
x = 0
if (x == 0):
    print("Zero")
elif (x == 1):
    print("One")
elif (x == 2):
    print("Two")
elif (x == 3):
    print("Three")
else:
    print("Some big number")

animals = ["cat", "dog", "bird", "elephant"]
for animal in animals:
    print(animal, len(animal))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(users.keys())  # dict_keys(['Hans', 'Éléonore', '景太郎'])
print(users.values())  # dict_values(['active', 'inactive', 'active'])
# dict_items([('Hans', 'active'), ('Éléonore', 'inactive'), ('景太郎', 'active')])
print(users.items())

active_users = {}
for name, status in users.items():  # items is equivalent of "entrySet"
    if (status == 'active'):
        active_users[name] = status

print(active_users)

# [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]
print(list(range(1, 1000, 100)))
print([*range(10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sentence = ["Ala", "ma", "kota"]
for index in range(len(sentence)):
    print(index, sentence[index])

# Alternatively, use enumerate(list) function:
for index, word in enumerate(sentence):
    print(index, word)

print(sum([1, 2, 3, 4]))  # 1 + 2 + 3 + 4
# print(sum('a', 'b'))  # TypeError: sum() can't sum strings [use ''.join(seq) instead]
print(sum(range(5)))  # 0 + 1 + 2 + 3 + 4

#  Prints 1 2 3 4 5
for i in range(1, 10):
    print(i)
    if (i == 5):
        break
else:
    print("ELSE")


# Prints 1 2 3 4 5 6 7 8 9 ELSE
# loop’s else clause runs when no break occurs
for i in range(1, 10):
    print(i)
else:
    print("ELSE")


for num in range(1, 11):
    if (num % 2 == 0):
        print(num, "Even number", sep=": ")
        continue  # continue continues going through loop, skipping operations below
    print(num, "Odd number", sep=": ")

# pass is kinda "Nothing" type from Kotlin

# Infinite loop
# while True:
#     pass  # Wait for keyboard interrupt

# Minimal possible class


class EmptyClass:
    pass


def very_complicated_function(*params):
    pass  # Works kinda like TODO from Kotlin


very_complicated_function("a")  # Nothing happens, as pass is doing nothing


# Pattern matching with "match"
# Only the first pattern that matches gets executed.
# It can also extract components (sequence elements or object attributes) from the value into variables.

def status_code_meaning(status_code):
    match status_code:
        case 400:
            return "Bad request"
        case 401:
            return "Unaothorized"
        case 402:
            return "Payment required"
        case 403:
            return "Forbidden"
        case _:
            return "Other code than 400, 401, 402, 403"


def general_status_code_meaning(status_code):
    match status_code:
        case 400 | 403:
            return "Auth problems"
        case 500 | 503:
            return "Server problems"
        case _:
            return "Other code than 400, 403, 500, 503"


point = (1, 2)  # tuple creation


def describe_point(p):
    match p:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"X={x}")
        case (0, y):
            print(f"Y={y}")
        case (x, y):
            print(f"X={x}, Y={y}")


describe_point(point)


class Point:
    x: int
    y: int


match point:
    # Guard - We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block.
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color('red')

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

# More about pattern matching: https://peps.python.org/pep-0636/


def empty_function():
    print("nothing interesting")


# Return without an expression argument returns None. Falling off the end of a function also returns None
print(empty_function())  # Returns 'None'

list_of_ints = [1, 2, 3]
list_of_ints.insert(0, -100)
print(list_of_ints)  # [-100, 1, 2, 3]


def fib_below(n) -> List:
    '''Return list of Fibonacci numbers which are lesser than n'''
    result = []
    first, second = 0, 1
    while (first < n):
        result.append(first)
        first, second = second, first + second
    return result


print(fib_below(1000))


def ask_ok(prompt, retries=3, reminder="Please try again"):
    while True:
        is_ok = input(prompt + "\n")
        if is_ok in ('y', 'yes', 'Y'):
            return True
        elif is_ok in ('n', 'no', 'N'):
            return False
        else:
            if (retries <= 0):
                raise ValueError("Invalid user response")
            retries -= 1
            print(reminder)


# print(ask_ok("Do you want to get a new job?"))
# print(ask_ok("Do you want to get a new job?", retries=3, reminder="valid inputs: y/n"))
# print(ask_ok("Do you want to get a new job?", reminder="valid inputs: y/n", retries=3))

default_argument_list = []


def function_with_default_argument(arg=default_argument_list):
    arg.append(1)


function_with_default_argument()
function_with_default_argument()
function_with_default_argument()

print(default_argument_list)  # [1, 1, 1]


def varargs_test(required_arg, *varargs, **keywords):
    print(required_arg)
    print("-" * 20)
    for arg in varargs:
        print(arg)
    print("-" * 20)
    for keyword in keywords:
        print(keyword)


varargs_test("required", "vararg1", "vararg2", kw1="1", kw2=2)
# required
# --------------------
# vararg1
# vararg2
# --------------------
# kw1
# kw2


def arguments_in_function(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


arguments_in_function("pos1", "pos2", "pos_or_kwd", kwd1="kwd1", kwd2="kwd2")
arguments_in_function(
    "pos1", "pos2", pos_or_kwd="pos_or_kwd", kwd1="kwd1", kwd2="kwd2")

# unpacking list


def unpack_list():
    x = [1, 3]
    return list(range(*x))


print(unpack_list())  # [1, 2]

print(1, 2, 3, **{'sep': '/', 'end': 'END\n'})  # 1/2/3END 🤯


def square_lamda(x: int) -> int: return x*x


print(square_lamda(2))  # 4


def power_lambda(a: int, b: int) -> int: return a**b


print(power_lambda(2, 10))  # 1024

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda element: element[1])
print(pairs)  # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


def documented_function():
    '''This function does absolutely nothing

    No need to explain more - just nothing
    '''
    pass


print(documented_function.__doc__)

print(str('String'))  # Stringify an object
print(str({'prop1': "value1"}))


def create_breakfast(fast: bool, toast: int, eggs: str = "yes!") -> str:
    # {'fast': <class 'bool'>, 'toast': <class 'int'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
    print(create_breakfast.__annotations__)
    if fast:
        return f"Very fast breakfast with {toast} toasts and eggs - {eggs}"
    else:
        return f"Very well cooked eggs - {eggs} with {toast} toasts"

# Very well cooked eggs - yes! with 4 toasts
print(create_breakfast(fast=False, toast=4))
