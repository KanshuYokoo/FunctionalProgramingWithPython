from typing import List

# --- IMPERATIVE STYLE ---
# How to compute: step-by-step mutation of state.
def imperative_sum(numbers: List[int]) -> int:
    total: int = 0
    for n in numbers:
        total = total + n  # mutate the variable at each step
    return total

# --- DECLARATIVE / FUNCTIONAL STYLE ---
# What the result is: expressed as a recursive relationship.
def functional_sum(numbers: List[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + functional_sum(numbers[1:])

# Alternatively, using Python's built-in pure function:
from functools import reduce
declarative_sum = lambda numbers: reduce(lambda acc, x: acc + x, numbers, 0)

print(imperative_sum([1, 2, 3, 4, 5]))   # 15
print(functional_sum([1, 2, 3, 4, 5]))   # 15
print(declarative_sum([1, 2, 3, 4, 5]))  # 15
