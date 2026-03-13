import sys
import itertools
from typing import Iterator, List

# 1. State and Imperative Loops
# The standard "imperative" way to iterate requires mutable state.

def sum_imperative(n: int) -> int:
    total: int = 0  # Re-assigned state
    for i in range(1, n + 1): # i is re-assigned state
        total += i
    return total

# 2. Recursion
# A pure functional loop without mutating variables.

def sum_recursive(n: int) -> int:
    # Base Case: Stop when n reaches 0
    if n == 0:
        return 0
    # Recursive Step
    return n + sum_recursive(n - 1)

# Mathematically equivalent to:
# S(0) = 0
# S(n) = n + S(n-1)

# 3. Python's Recursion Depth Limits
# Python does not support Tail Call Optimization natively.
# If n is too large, sum_recursive will hit the recursion limit.

print(f"Current recursion limit is: {sys.getrecursionlimit()}")
# Running sum_recursive(2000) would likely throw a RecursionError.


# 4. Itertools: The Functional Engine of Python
# To iterate functionally in Python over large or infinite sequences safely,
# we use iterators/generators. Iterators only compute exactly what is asked.

# Using itertools.count to represent an infinite sequence of numbers starting from 1
infinite_numbers: Iterator[int] = itertools.count(start=1)

# Using itertools.islice to take the first 5 elements from that infinite generator
first_five: Iterator[int] = itertools.islice(infinite_numbers, 5)

# We can then sum them using the built-in, optimized C-loop based sum()
# which behaves like a fold (reduce).
sum_first_five: int = sum(first_five)

# 5. Generators as custom streams
# Generators allow us to create our own lazy sequences.

def generate_fibonacci() -> Iterator[int]:
    """An infinite generator of Fibonacci numbers."""
    a, b = 0, 1
    while True: # Infinite lazy loop
        yield a
        a, b = b, a + b

# Generating an infinite stream
fib_stream: Iterator[int] = generate_fibonacci()

# Taking the first 10 Fibonacci numbers
first_10_fibs: List[int] = list(itertools.islice(fib_stream, 10))

if __name__ == "__main__":
    print(f"Imperative sum(10): {sum_imperative(10)}")
    print(f"Recursive sum(10): {sum_recursive(10)}")
    print(f"Sum first five of infinite count: {sum_first_five}")
    print(f"First 10 Fibonaccis: {first_10_fibs}")
