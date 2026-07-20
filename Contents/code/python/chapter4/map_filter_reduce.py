from functools import reduce
from typing import List

# Input sequence
numbers: List[int] = [1, 2, 3, 4, 5]

# 1. Using functional built-ins (map, filter, reduce)
squares_map: List[int] = list(map(lambda x: x * x, numbers))
# squares_map == [1, 4, 9, 16, 25]

evens_filter: List[int] = list(filter(lambda x: x % 2 == 0, numbers))
# evens_filter == [2, 4]

total_sum: int = reduce(lambda x, y: x + y, numbers, 0)
# total_sum == 15

# 2. Using idiomatic Python alternatives (List Comprehensions)
squares_comp: List[int] = [x * x for x in numbers]
evens_comp: List[int] = [x for x in numbers if x % 2 == 0]

if __name__ == "__main__":
    print(f"Squares (map): {squares_map}")
    print(f"Evens (filter): {evens_filter}")
    print(f"Total Sum (reduce): {total_sum}")
    print(f"Squares (comp): {squares_comp}")
    print(f"Evens (comp): {evens_comp}")
