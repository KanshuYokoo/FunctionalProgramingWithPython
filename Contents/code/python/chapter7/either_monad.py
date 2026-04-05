from typing import TypeVar, Generic, Callable

L = TypeVar('L') # Left type (Error)
R = TypeVar('R') # Right type (Success)
R2 = TypeVar('R2')

class Either(Generic[L, R]):
    def __init__(self, is_left: bool, left_val: L = None, right_val: R = None):
        self.is_left = is_left
        self.left_val = left_val
        self.right_val = right_val

    @staticmethod
    def Left(val: L) -> 'Either[L, R]':
        return Either(True, left_val=val)

    @staticmethod
    def Right(val: R) -> 'Either[L, R]':
        return Either(False, right_val=val)

    def bind(self, f: Callable[[R], 'Either[L, R2]']) -> 'Either[L, R2]':
        if self.is_left:
            # Short-circuit, retaining the error
            return Either.Left(self.left_val)
        return f(self.right_val)
        
    def __repr__(self):
        if self.is_left:
            return f"Left({self.left_val})"
        return f"Right({self.right_val})"

# Usage example chaining operations that might fail
def divide_by(y: int) -> Callable[[int], Either[str, int]]:
    def inner(x: int) -> Either[str, int]:
        if y == 0:
            return Either.Left("Cannot divide by zero")
        return Either.Right(x // y)
    return inner

# Chaining successful path: 100 / 2 / 5
success_chain = Either.Right(100).bind(divide_by(2)).bind(divide_by(5))
print(success_chain) # Right(10)

# Chaining failing path: 100 / 0 / 5
fail_chain = Either.Right(100).bind(divide_by(0)).bind(divide_by(5))
print(fail_chain) # Left(Cannot divide by zero)
