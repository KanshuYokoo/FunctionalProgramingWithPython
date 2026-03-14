# Workthrough Chapter 6: Iteration & Recursion

## Section Breakdown

1. **The Problem with Loops**
   - Imperative loops (like `for` and `while`) inherently rely on mutable state (e.g., updating a counter variable `i`). 
   - Pure functional programming forbids mutable state. So, how do we repeat actions?

2. **Recursion: The Functional Loop**
   - Concept: A function that calls itself until it reaches a base case.
   - Mathematical elegance: Recurrence relations (e.g., the Fibonacci sequence) map directly to recursive functions without translation.
   - Diagramming the call stack.

3. **Python's Limitation: Recursion Depth**
   - Python is not designed to be a strictly pure functional language. Deep recursion will result in a `RecursionError`.
   - Discuss why: Python does *not* support Tail Call Optimization (TCO).

4. **Itertools: Python's Functional Looping Engine**
   - If we shouldn't use deep recursion in Python, and we want to avoid stateful `for` loops, what is the middle ground? Generators and the `itertools` module.
   - Lazy evaluation: Generating values only when they are needed.
   - Example using `itertools.count` as an "infinite" list abstraction.

5. **Haskell: Native Recursion and Infinite Lists**
   - Haskell *does* support Tail Call Optimization, meaning tail-recursive functions can run infinitely without blowing up the stack.
   - Showing Haskell's pattern matching and guard clauses for clean base-case declarations.
   - Haskell's profound lazy evaluation allows us to declare infinite lists structurally (e.g., `[1..]`), map over them, and only take what we need using functions like `take`.

## Resources Created

- **Text:** `Contents/text/chapter6_iteration/chapter6_main.tex`
- **Python:** `Contents/code/python/chapter6/iteration_recursion.py`
- **Haskell:** `Contents/code/haskel/chapter6/iteration_recursion.hs`
