from typing import Callable

# HOF that takes a function and returns its numerical derivative
def derivative(f: Callable[[float], float], dx: float = 1e-5) -> Callable[[float], float]:
    """Computes the numerical derivative of f with step size dx."""
    return lambda x: (f(x + dx) - f(x)) / dx

if __name__ == "__main__":
    # Define f(x) = x^2
    def square(x: float) -> float:
        return x * x
        
    # f'(x) should be 2x
    f_prime = derivative(square)
    
    # f'(3) = 2(3) = 6
    print(f"Derivative of x^2 at x=3: {f_prime(3.0):.4f}") # Approx 6.0000
    
    # Define f(x) = x^3
    # f'(x) should be 3x^2
    f_prime_cube = derivative(lambda x: x * x * x)
    
    # f'(2) = 3(2^2) = 12
    print(f"Derivative of x^3 at x=2: {f_prime_cube(2.0):.4f}") # Approx 12.0000
