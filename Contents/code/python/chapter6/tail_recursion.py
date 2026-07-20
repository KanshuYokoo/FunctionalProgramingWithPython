# 1. Factorial: Non-Tail Recursive
# The multiplication operation occurs after the recursive call returns.
# GHC (Haskell) cannot optimize this, and Python grows the call stack.

def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    # Multiplication is pending; this is not a tail call.
    return n * factorial_recursive(n - 1)


# 2. Factorial: Tail Recursive (Accumulator Pattern)
# We pass the running product as an accumulator argument.
# The recursive call is the final operation.

def factorial_tail_recursive(n: int, accumulator: int = 1) -> int:
    if n == 0:
        return accumulator
    # The return value is exactly the return value of the recursive call.
    # No pending operations remain.
    return factorial_tail_recursive(n - 1, n * accumulator)


# 3. Greatest Common Divisor (GCD): Naturally Tail Recursive
# Euclid's algorithm naturally places the recursive call in the tail position.
# No accumulator is needed because there are no pending operations on return.

def gcd_euclid(a: int, b: int) -> int:
    if b == 0:
        return a
    # Naturally in the tail position
    return gcd_euclid(b, a % b)


if __name__ == "__main__":
    # Test values
    fact_val: int = 5
    print(f"factorial_recursive({fact_val}) = {factorial_recursive(fact_val)}")
    print(f"factorial_tail_recursive({fact_val}) = {factorial_tail_recursive(fact_val)}")
    
    a_val, b_val = 48, 18
    print(f"gcd_euclid({a_val}, {b_val}) = {gcd_euclid(a_val, b_val)}")
