from typing import Callable, TypeVar

# Type variables for curry/uncurry: A -> B -> C
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

# curry: ((A, B) -> C) -> (A -> (B -> C))
def curry(f: Callable[[A, B], C]) -> Callable[[A], Callable[[B], C]]:
    """Converts a two-argument function into a curried function."""
    return lambda x: lambda y: f(x, y)

# uncurry: (A -> (B -> C)) -> ((A, B) -> C)
def uncurry(g: Callable[[A], Callable[[B], C]]) -> Callable[[A, B], C]:
    """Converts a curried function back to a two-argument function."""
    return lambda x, y: g(x)(y)

# Example 1: Basic addition
def add(x: int, y: int) -> int:
    return x + y

# Example 2: Logging configurator
def log_message(level: str, message: str) -> None:
    print(f"[{level}] {message}")

if __name__ == "__main__":
    # Currying addition
    curried_add = curry(add)
    add_five = curried_add(5)
    print(f"add(5)(10) = {add_five(10)}")  # 15

    # Uncurrying addition
    uncurried_add = uncurry(curried_add)
    print(f"add(5, 10) = {uncurried_add(5, 10)}")  # 15

    # Currying logging
    curried_log = curry(log_message)
    info_log = curried_log("INFO")
    error_log = curried_log("ERROR")

    info_log("Application started successfully.")
    error_log("Failed to connect to database.")
