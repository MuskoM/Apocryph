# 1 Capitalize all of the pet names and print the list
from functools import reduce

my_pets = ['sisi', 'bibi', 'titi', 'carla']


def upper(item):
    return item.upper()


my_big_pets = list(map(upper, my_pets))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

zipped = list(zip(my_strings, sorted(my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over50(item):
    return item > 50


filtered_scores = list(filter(over50, scores))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulate(tots, item):
    return tots + item


reduced = reduce(accumulate, (my_numbers + scores))

print(f'Pets: {my_big_pets}\n Zipped: {zipped} \nFiltered: {filtered_scores} \nReduced: {reduced}')

# def multiply_by2(item):
#     return item*2

# map with lambda
print(list(map(lambda item: item * 2, scores)))

print(list(filter(lambda item: item > 50, scores)))

mylist = [4, 5, 6]

print(list(map(lambda item: item ** 2, mylist)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)

# List Comprehensions
# Same thing for sets
quick_list = [char for char in "Hello"]
conditional_quick_list = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(conditional_quick_list)

# Dict Comprehensions

my_dict = {value[0]: value[1] for value in a}
print(my_dict)

some_list = [item for item in 'abcbdmnn']
duplicates = {item for item in some_list if some_list.count(item) >= 2}
print(duplicates)


# Decorators
def my_decorator(func):
    def wrap_func(*args):
        print(">>>>>>>>>")
        func(*args)
        print(">>>>>>>>>")
    return wrap_func


@my_decorator
def greeter(*args):
    print(*args)


greeter('smile', 'preety', ':)')