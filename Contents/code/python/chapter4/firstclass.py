from typing import Callable, List

# A simple pure function
def add_one(x: int) -> int:
    return x + 1

def multiply_by_two(x: int) -> int:
    return x * 2

# HIGHER-ORDER FUNCTION
# Takes a function 'f' as an argument.
def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))

# We can pass different functions like data
print(apply_twice(add_one, 5))         # (5 + 1) + 1 = 7
print(apply_twice(multiply_by_two, 5)) # (5 * 2) * 2 = 20

# MAP, FILTER, REDUCE in Python
numbers: List[int] = [1, 2, 3, 4, 5]

# map applies a function to every item
squares = list(map(lambda x: x * x, numbers))
print(squares) # [1, 4, 9, 16, 25]

# filter keeps items where the function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4]
