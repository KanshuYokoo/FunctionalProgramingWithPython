from typing import List, Dict, Set

data: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehension: Map and Filter combined
even_squares: List[int] = [x * x for x in data if x % 2 == 0]
print("Even squares:", even_squares)

# Set Comprehension: Removing duplicates while transforming
word_list: List[str] = ["apple", "banana", "apple", "cherry"]
unique_lengths: Set[int] = {len(word) for word in word_list}
print("Unique word lengths:", unique_lengths)

# Dict Comprehension: Creating a mapping
names: List[str] = ["Alice", "Bob", "Charlie"]
name_lengths: Dict[str, int] = {name: len(name) for name in names}
print("Name lengths:", name_lengths)

# Generator Expression: Lazy evaluation (similar to Haskell's lazy lists)
lazy_squares = (x * x for x in data)
print("First lazy square:", next(lazy_squares))
print("Second lazy square:", next(lazy_squares))
