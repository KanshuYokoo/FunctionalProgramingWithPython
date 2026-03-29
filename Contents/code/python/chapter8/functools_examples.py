from functools import partial, lru_cache
from typing import Callable

def power(base: int, exp: int) -> int:
    return base ** exp

# Using functools.partial to create a new function that squares a number (fixes exp=2)
# The type here defines the new signature: takes one int, returns one int.
square: Callable[[int], int] = partial(power, exp=2)
cube: Callable[[int], int] = partial(power, exp=3)

print("Square of 5:", square(5))
print("Cube of 3:", cube(3))

# Using lru_cache for memoization of a pure recursive function
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fast execution due to caching of repetitive sub-problems
print("50th Fibonacci number:", fibonacci(50))
