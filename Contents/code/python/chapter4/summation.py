from typing import Callable

# Higher-order function for mathematical summation: sum_{n=a}^{b} f(n)
def sum_series(f: Callable[[int], int], a: int, b: int) -> int:
    """Computes the sum of f(n) from n = a to b."""
    return sum(f(n) for n in range(a, b + 1))

if __name__ == "__main__":
    # Sum of identity function: 1 + 2 + 3 + 4 + 5 = 15
    sum_identity = sum_series(lambda x: x, 1, 5)
    
    # Sum of squares: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
    sum_squares = sum_series(lambda x: x * x, 1, 5)
    
    # Sum of cubes: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225
    sum_cubes = sum_series(lambda x: x * x * x, 1, 5)
    
    print(f"Sum of identity (1..5): {sum_identity}")
    print(f"Sum of squares (1..5): {sum_squares}")
    print(f"Sum of cubes (1..5): {sum_cubes}")
