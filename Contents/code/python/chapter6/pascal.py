from functools import lru_cache

# 1. Tree Recursion
# A translation of the recursive Pascal's triangle algorithm.
# Since the function branches twice, this creates a binary call tree.
# This runs in exponential O(2^r) time.

def pascal(c: int, r: int) -> int:
    # Base Cases: Edge values of the triangle are always 1
    if c == 0 or c == r:
        return 1
    # Recursive Step
    return pascal(c - 1, r - 1) + pascal(c, r - 1)


# 2. Optimized Tree Recursion (Memoization)
# Because pascal_memoized is pure (free of side effects), we can cache results.
# lru_cache stores results for previous argument combinations,
# reducing the complexity from O(2^r) to O(r^2).

@lru_cache(maxsize=None)
def pascal_memoized(c: int, r: int) -> int:
    if c == 0 or c == r:
        return 1
    return pascal_memoized(c - 1, r - 1) + pascal_memoized(c, r - 1)


if __name__ == "__main__":
    # Computing element at column 2, row 4 (which is 6)
    print(f"pascal(2, 4) = {pascal(2, 4)}")
    
    # Printing the first 5 rows of the triangle
    print("Pascal's Triangle (first 5 rows):")
    for row in range(5):
        row_vals = [pascal_memoized(col, row) for col in range(row + 1)]
        print(" ".join(map(str, row_vals)).center(20))
