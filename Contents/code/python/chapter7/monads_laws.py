from typing import TypeVar, Generic, Callable, Optional

A = TypeVar('A')
B = TypeVar('B')

class Maybe(Generic[A]):
    def __init__(self, value: Optional[A]):
        self.value = value

    @staticmethod
    def unit(value: A) -> 'Maybe[A]':
        """The 'return' or 'pure' function. Wraps a value in the Monad."""
        return Maybe(value)

    def bind(self, f: Callable[[A], 'Maybe[B]']) -> 'Maybe[B]':
        if self.value is None:
            return Maybe(None)
        return f(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Maybe):
            return NotImplemented
        return self.value == other.value

# Test variables
def f(x: int) -> Maybe[str]: return Maybe(str(x))
def g(s: str) -> None: return Maybe(len(s)) # Wait, should return Maybe[int]. Fixing:
def g_real(s: str) -> Maybe[int]: return Maybe(len(s))

x = 5
m = Maybe(5)

# 1. Left Identity
# unit(x).bind(f) == f(x)
assert Maybe.unit(x).bind(f) == f(x)

# 2. Right Identity
# m.bind(unit) == m
assert m.bind(Maybe.unit) == m

# 3. Associativity
# m.bind(f).bind(g) == m.bind(lambda x: f(x).bind(g))
assert m.bind(f).bind(g_real) == m.bind(lambda v: f(v).bind(g_real))

print("Monad Laws hold true.")
