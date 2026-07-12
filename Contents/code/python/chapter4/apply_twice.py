from typing import Callable

# A simple pure function
def add_one(x: int) -> int:
    return x + 1

def multiply_by_two(x: int) -> int:
    return x * 2

# HIGHER-ORDER FUNCTION
# Takes a function 'f' and an integer 'x'
def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))

if __name__ == "__main__":
    print(apply_twice(add_one, 5))         # (5 + 1) + 1 = 7
    print(apply_twice(multiply_by_two, 5)) # (5 * 2) * 2 = 20
