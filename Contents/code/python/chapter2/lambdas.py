from typing import Callable

# A standard named function
def add_one_named(x: int) -> int:
    return x + 1

# The Lambda Calculus equivalent: an anonymous function
# Syntax: lambda bound_variable: body
add_one_lambda: Callable[[int], int] = lambda x: x + 1

# Beta-reduction in Python (Application)
# (lambda x: x + 1)(5)
result = (lambda x: x + 1)(5)
print(result) # Output: 6
