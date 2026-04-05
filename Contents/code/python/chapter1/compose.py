from typing import Callable, TypeVar

# We define generic types A, B, C for our Objects
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

def compose(g: Callable[[B], C], f: Callable[[A], B]) -> Callable[[A], C]:
    """
    Returns the composition of g and f (g composed with f).
    Recall that f maps A -> B, and g maps B -> C.
    The result maps A -> C.
    """
    return lambda x: g(f(x))

# Example Morphisms
def length(s: str) -> int:
    return len(s)

def is_even(n: int) -> bool:
    return n % 2 == 0

# (is_even composed with length) : str -> bool
is_even_length: Callable[[str], bool] = compose(is_even, length)

print(is_even_length("Category")) # True (8 is even)
