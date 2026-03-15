from typing import TypeVar, Generic, Callable, Optional, List

T = TypeVar('T')
U = TypeVar('U')

class Maybe(Generic[T]):
    """
    A simple Maybe class to demonstrate a computational context (Functor).
    It represents either a value of type T, or nothing.
    """
    def __init__(self, value: Optional[T]):
        self._value = value

    @property
    def is_present(self) -> bool:
        return self._value is not None

    def map(self, func: Callable[[T], U]) -> 'Maybe[U]':
        """
        The fmap operation!
        Takes a function from T -> U, and applies it to the value inside
        the Maybe context, returning a new Maybe[U].
        If this Maybe is empty, it does nothing and returns an empty Maybe.
        """
        if self.is_present:
            # We must type ignore here or cast, as the type checker
            # can't easily prove self._value is not None from the property
            return Maybe(func(self._value))  # type: ignore
        return Maybe(None)

    def __repr__(self) -> str:
        return f"Just({self._value})" if self.is_present else "Nothing()"


# --- Usage Example ---

def square(x: int) -> int:
    return x * x

def int_to_str(x: int) -> str:
    return f"Number: {x}"

# 1. A Maybe context holding a value
just_5 = Maybe(5)
# Lifting 'square' into the context
just_25 = just_5.map(square)
print(f"just_5 mapped with square: {just_25}")

# 2. An empty Maybe context
nothing: Maybe[int] = Maybe(None)
# Mapping over Nothing safely does... nothing! No NoneType errors.
still_nothing = nothing.map(square)
print(f"nothing mapped with square: {still_nothing}")

# 3. Chaining functor maps
chained_result = just_5.map(square).map(int_to_str)
print(f"Chained functor mapping: {chained_result}")

# 4. Built-in Python Lists are also Functors!
numbers: List[int] = [1, 2, 3, 4]
# Python's built-in map() is the fmap operation for iterables.
squared_numbers = list(map(square, numbers))
print(f"List functor mapping: {squared_numbers}")
