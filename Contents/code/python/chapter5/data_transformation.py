from typing import List, Callable, TypeVar, Iterable
from functools import reduce

A = TypeVar('A')
B = TypeVar('B')

# 1. Mapping (Data Transformation)
# Applying a function to every item in an iterable.

numbers: List[int] = [1, 2, 3, 4, 5]

# Using built-in map
def square(x: int) -> int:
    return x * x

squared_numbers_map: List[int] = list(map(square, numbers))
# Expected: [1, 4, 9, 16, 25]

# Pythonic alternative: List Comprehension
squared_numbers_comp: List[int] = [square(x) for x in numbers]


# 2. Filtering
# Keeping items that satisfy a predicate.

def is_even(x: int) -> bool:
    return x % 2 == 0

# Using built-in filter
even_numbers_filter: List[int] = list(filter(is_even, numbers))
# Expected: [2, 4]

# Pythonic alternative: List Comprehension with condition
even_numbers_comp: List[int] = [x for x in numbers if is_even(x)]


# 3. Reducing (Folding)
# Accumulating items down to a single value.

def add(x: int, y: int) -> int:
    return x + y

# Using functools.reduce
sum_reduce: int = reduce(add, numbers)
# Expected: 15 (1+2+3+4+5)

# With an initial value
sum_reduce_initial: int = reduce(add, numbers, 10)
# Expected: 25 (10+1+2+3+4+5)

# Pythonic alternative: Built-in function
sum_builtin: int = sum(numbers)


# 4. Defining our own Map and Filter to see how they work

def my_map(func: Callable[[A], B], iterable: Iterable[A]) -> List[B]:
    result : List[B] = []
    for item in iterable:
        result.append(func(item))
    return result

def my_filter(predicate: Callable[[A], bool], iterable: Iterable[A]) -> List[A]:
    result : List[A] = []
    for item in iterable:
        if predicate(item):
            result.append(item)
    return result

# 5. Combining Map and Filter
# Square only the even numbers

# Functional style
squared_evens_func: List[int] = list(map(square, filter(is_even, numbers)))

# List Comprehension style
squared_evens_comp: List[int] = [square(x) for x in numbers if is_even(x)]

if __name__ == "__main__":
    print(f"Original: {numbers}")
    print(f"Map (square): {squared_numbers_map}")
    print(f"Filter (even): {even_numbers_filter}")
    print(f"Reduce (sum): {sum_reduce}")
    print(f"Combined (square evens): {squared_evens_func}")
