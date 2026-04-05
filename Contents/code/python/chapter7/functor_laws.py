from typing import TypeVar, Generic, Callable, Optional

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

class Maybe(Generic[A]):
    def __init__(self, value: Optional[A]):
        self.value = value

    def map(self, f: Callable[[A], B]) -> 'Maybe[B]':
        if self.value is None:
            return Maybe(None)
        return Maybe(f(self.value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Maybe):
            return NotImplemented
        return self.value == other.value

# 1. Identity Law
# fmap id = id
def identity(x: A) -> A:
    return x

box = Maybe(5)
assert box.map(identity) == box

# 2. Composition Law
# fmap (g . f) = fmap g . fmap f
def add_one(x: int) -> int: return x + 1
def square(x: int) -> int: return x * x

def compose(g: Callable[[B], C], f: Callable[[A], B]) -> Callable[[A], C]:
    return lambda x: g(f(x))

assert box.map(compose(square, add_one)) == box.map(add_one).map(square)
print("Functor Laws hold true.")
