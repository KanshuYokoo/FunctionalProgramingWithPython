from typing import Callable, TypeVar

# Type variables for composition: A -> B -> C
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

# HOF that returns the composition of two functions: (g o f)(x) = g(f(x))
def compose(g: Callable[[B], C], f: Callable[[A], B]) -> Callable[[A], C]:
    return lambda x: g(f(x))

if __name__ == "__main__":
    # Add one: x + 1
    add_one = lambda x: x + 1
    # Square: x^2
    square = lambda x: x * x
    
    # (square o add_one)(x) = (x + 1)^2
    square_of_add_one = compose(square, add_one)
    
    # (4 + 1)^2 = 25
    print(f"Composition (square o add_one)(4): {square_of_add_one(4)}")
