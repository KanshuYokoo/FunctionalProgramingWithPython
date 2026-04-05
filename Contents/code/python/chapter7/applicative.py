from typing import TypeVar, Generic, Callable, Optional

A = TypeVar('A')
B = TypeVar('B')

class Maybe(Generic[A]):
    def __init__(self, value: Optional[A]):
        self.value = value
        
    def __repr__(self) -> str:
        return f"Just({self.value})" if self.value is not None else "Nothing"

    def apply(self, wrapped_func: 'Maybe[Callable[[A], B]]') -> 'Maybe[B]':
        """
        The Applicative operation (<*>).
        Takes a Box containing a function, and applies it to the Box containing a value.
        """
        if self.value is None or wrapped_func.value is None:
            return Maybe(None)
        return Maybe(wrapped_func.value(self.value))

# A function trapped in a box
boxed_func = Maybe(lambda x: x * 10)
boxed_val = Maybe(5)

# We cannot easily use map here, because the function is in a box. 
# We use apply (Applicative):
result = boxed_val.apply(boxed_func)
print(result) # Just(50)
