from collections import deque
from math import pi, isnan

test_list = [1, 2, 3]

test_list.append(4)  # [1, 2, 3, 4]
test_list.extend([5, 6, 7])  # [1, 2, 3, 4, 5, 6, 7]
test_list.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6, 7]
test_list.remove(3)  # [0, 1, 2, 4, 5, 6, 7]
test_list.pop()  # 7 -> [0, 1, 2, 4, 5, 6]
test_list.pop(0)  # 0 -> [1, 2, 4, 5, 6]
test_list.count(0)  # 0
test_list.sort(key=lambda x: x)

# Using List as Stack
stack = []
stack.append(3)  # [3]
stack.append(2)  # [3, 2]
stack.append(1)  # [3, 2, 1]
stack.pop()  # 1 -> [3, 2]
stack.pop()  # 2 -> [3]
stack.pop()  # 3 -> []

# Using Queues
queue = deque(['B', 'C'])  # ['B', 'C']
queue.append('D')  # ['B', 'C', 'D']
queue.appendleft('A')  # ['A', 'B', 'C', 'D']
queue.extend(['a', 'b', 'c', 'd'])  # ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
# It's gonna be reversed - ['1', '2', '3', 'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']
queue.extendleft(['3', '2', '1'])
print(queue)  # deque(['1', '2', '3', 'A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'])

# List comprehensions

# From wikipedia:
# A list comprehension is a syntactic construct available in some programming languages
# for creating a list based on existing lists. It follows the form of the mathematical
# set-builder notation (set comprehension) as distinct from the use of map and filter functions.

squares0 = []
for i in range(1, 10):
    squares0.append(i * i)
print(squares0)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = list(map(lambda x: x*x, range(1, 10)))
print(squares2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

squares3 = [x*x for x in range(1, 10)]
print(squares3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

pairs = [(x, y) for x in [1, 2, 3] if x > 1 for y in [3, 4, 1] if x != y]
print(pairs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# create a list of 2-tuples like (number, square)
[(x, x*x) for x in range(1, 10)]

# flatten a list using a listcomp with two 'for'
nested_vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_vec = [n for nested in nested_vec for n in nested]
print(flatten_vec)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[s.strip() for s in freshfruit]  # ['banana', 'loganberry', 'passion fruit']

pis = [round(pi, i) for i in range(1, 6)]
print(pis)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
print(transposed_matrix)

print(*matrix)  # [1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]
transposed_matrix2 = list(zip(*matrix))
print(transposed_matrix2)  # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

list_to_delete = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del list_to_delete[9]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
del list_to_delete[1:5]  # [0, 5, 6, 7, 8]
del list_to_delete[:]  # []
del list_to_delete
# print(list_to_delete)  # NameError: name 'list_to_delete' is not defined

# Sequence - lists, tuples, ranges
tuple1 = 'Szymon', 1, ['a', 'b', 'c']  # ('Szymon', 1, ['a', 'b', 'c'])
tuple1[2][1] = 'd'  # ('Szymon', 1, ['a', 'd', 'c'])
len(tuple1)  # 3

empty_tuple = ()
single_element_tuple = "Single",
print(empty_tuple)
print(single_element_tuple)

# Tuple packing
tuple_packed = 1, 'a', 'b'

# Sequence unpacking
number, char1, char2 = tuple_packed

# Multiple assignement is tuple packing + sequence unpacking
elem1, elem2 = 1, 'b'

# What about sequence unpacking on range?
e1, e2, e3 = range(3)
print(e1, e2, e3)  # 0 1 2

# Sets
# Removed duplicates - # {'perry', 'potato', 'tomato', 'peach', 'apple'}
basket = {'apple', 'perry', 'apple', 'peach', 'tomato', 'potato', 'potato'}
is_orange_in_basket = 'orange' in basket  # false
empty_basket = set()
empty_basket.add(1)
empty_basket.add('1')
print(empty_basket)  # {'1', 1}

expecto_patronum = set('expecto patronum')
# {'n', 'u', 'r', 'e', ' ', 'x', 'o', 'a', 't', 'm', 'c', 'p'}
print(expecto_patronum)
avada_kedavra = set('avada kedavra')
print(avada_kedavra)  # {'v', 'a', 'e', 'k', 'd', 'r', ' '}

# Operations on sets:

# Difference
# {'m', 'o', 'n', 't', 'p', 'u', 'x', 'c'}
diff1 = expecto_patronum - avada_kedavra
diff2 = avada_kedavra - expecto_patronum  # {'k', 'd', 'v'}
print(diff1 != diff2)  # True

# Symetric difference - letters in A or B, but not both
# {'u', 'd', 'k', 'p', 'n', 't', 'o', 'v', 'm', 'x', 'c'}
symetric_diff = expecto_patronum ^ avada_kedavra

# Union
# {'u', 'd', 'p', 'e', 'k', ' ', 'n', 'r', 't', 'o', 'v', 'a', 'm', 'x', 'c'}
union = expecto_patronum | avada_kedavra

# Intersection
# {'e', 'r', 'a', ' '}
intersection = expecto_patronum & avada_kedavra

# Set comprehension - build a set from other iterable

# {1, 2, 3, 5}
set_from_comprehension = {x for x in [1, 2, 3, 1, 2, 5, 9, 8] if x < 6}

# {'f', 'h', 'b', 'e', 'g'}
other_set_from_comprehension = {x for x in 'abcdefghabcde' if x not in 'acdc'}

# Dictionaries
# Empty dictionary
empty_dictionary = {}

dictionary = {'key': 'value', 'key': 'value2'}  # {'key': 'value2'}
dictionary['key2'] = 'value2'  # {'key': 'value2', 'key2': 'value2'}
dictionary['key'] = 'v'  # {'key': 'v', 'key2': 'value2'}
del dictionary['key']  # {'key2': 'value2'}
# dictionary['key']  # KeyError: 'key'

spell_levels = {'lumos': 1, 'vingardium leviosa': 1,
                'opugno': 5, 'expecto patronum': 9}
list(spell_levels)  # like Kotlin's spell_levels.keys()
# sorted - sorts elements in iterable, returning new one (not modifying existing one)
print(sorted(spell_levels, key=lambda x: x[1]))  # sorted by spell difficulty

is_dretwota_in_spell_levels = 'dretwota' in spell_levels  # False
is_accio_not_in_spell_levels = 'accio' not in spell_levels  # True

# {1: 'a', 2: 'b', 3: 'c'}
dictionary_from_list_of_pairs = dict([(1, 'a'), (2, 'b'), (3, 'c')])

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
dict_comprehension = {x: x*x for x in range(5)}

# {'name': 'Szymon', 'surname': 'Marcinkiewicz'}
dict_from_kwargs = dict(name="Szymon", surname="Marcinkiewicz")

# Iterating
for key, value in dict_from_kwargs.items():
    print(key, value)

# 0 name
# 1 surname
for index, elem in enumerate(dict_from_kwargs):
    print(index, elem)

# 0 ('name', 'Szymon')
# 1 ('surname', 'Marcinkiewicz')
for index, elem in enumerate(dict_from_kwargs.items()):
    print(index, elem)

for index, elem in enumerate(['a', 'b', 'c', 'd', 'e']):
    print(index, elem, sep=' : ')

list_of_characters = ['a', 'b', 'c', 'd', 'e']
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
list(enumerate(list_of_characters))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
[(index, element) for index, element in enumerate(list_of_characters)]

list_of_ints = [1, 2, 3, 4, 5]

# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
zipped_list = list(zip(list_of_ints, list_of_characters))
for i, c in zipped_list:
    print(i, c)

# Reverse
reversed_list_of_ints = list(reversed(list_of_ints))  # [5, 4, 3, 2, 1]
reversed_range = list(reversed(range(1, 10, 2)))  # [9, 7, 5, 3, 1]

basket_list = ['apple', 'pear', 'plum', 'orange',
               'peach', 'banana', 'dragon fruit',
               'litchi', 'pear', 'plum', 'grapes',
               'pineapple', 'watermelon', 'apple']

# Sorted elements of basket_list - new instance of list
sorted(basket_list)

# Sorted elements with removed duplicates
sorted(set(basket_list))

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_non_nan = [x for x in raw_data if not isnan(x)]

# Boolean operators
false_1 = True and False
true_1 = True or False
true_2 = True and not False
true_3 = 1 < 2 == 1  # (one less than two) and (one equal to one)
false_2 = True and not True or False  # (True and (not True)) or False
false_3 = False and True and True  # False and (x) -> x is not evaluated

string1, string2, string3 = '', 'Wroclaw', 'London'
non_null_string = string1 or string2 or string3
print(non_null_string)  # Wroclaw

# Assignment
test_number = 1 + 2

# Expression
# Walrus operator - assignment of value in expression
(test_number_in_expression := 1 + 2)

# Comparing sequences
(1, 2, 3) < (1, 2, 4)  # type: ignore
[1, 2, 4] > [1, 2, 3]  # type: ignore
'ABC' < 'Pascal' > 'C' < 'Python'  # type: ignore
(1, 2, 4) > (1, 2, 3, 4)  # type: ignore
(1, 2) < (1, 2, -1)  # type: ignore
(1.0, 2.0, 3.0) == (1, 2, 3)  # type: ignore
(1, 2, ('abc', 'a'), 4) > (1, 2, ('aa', 'ab'))  # type: ignore
