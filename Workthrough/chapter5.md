# Workthrough Chapter 5: Data Transformation

## Section Breakdown

1. **Introduction to Data Transformation**
   - The functional paradigm shifts focus from *how* to iterate (imperative loops) to *what* data transformation is applied to a collection (declarative mapping, filtering, reducing).
   - Core functional primitives: `map`, `filter`, and `reduce` (or `fold`).

2. **Mapping (`map`)**
   - Concept: Applying a single function to every element in an iterable.
   - Python: Using the built-in `map()` function. Contrast with list comprehensions (which are often more "Pythonic").
   - Haskell: Using the `map` function. The type signature `(a -> b) -> [a] -> [b]` is fundamentally important here. It illustrates that `map` transforms a list of type `a` to a list of type `b`.

3. **Filtering (`filter`)**
   - Concept: Removing items from a collection based on a predicate function (a function returning a boolean).
   - Python: Using the built-in `filter()` and using generator expressions.
   - Haskell: Using the `filter` function. Type signature `(a -> Bool) -> [a] -> [a]`.

4. **Reducing/Folding (`reduce` / `fold`)**
   - Concept: Crushing an iterable down into a single cumulative value using an accumulator function.
   - Analogy: Snowball rolling down a hill, picking up more snow (accumulating).
   - Python: Requires `functools.reduce`. Emphasize that Guido van Rossum preferred explicit loops or comprehensions over `reduce`, making it a point of contention in Python's functional design.
   - Haskell: Deep dive into `foldl` (left fold) and `foldr` (right fold). Show how `foldr` is lazy and can operate on infinite lists. Type signature of `foldl`: `(b -> a -> b) -> b -> [a] -> b`.

5. **List Comprehensions**
   - Combining `map` and `filter` into a single, highly readable syntax.
   - Origin: Derived from mathematical set-builder notation.
   - Compare Python's `[f(x) for x in xs if p(x)]` with Haskell's `[f x | x <- xs, p x]`.

6. **Mathematical Perspective: Functors (Again)**
   - Reinforcing the definition of a Functor from Chapter 4.
   - A list is a Functor because we can map over it. `map` is the mechanism that "lifts" ordinary functions to operate on elements within the context of a list.

## Resources Created

- **Text:** `Contents/text/chapter5_datatransformation/chapter5_main.tex`
- **Python:** `Contents/code/python/chapter5/data_transformation.py`
- **Haskell:** `Contents/code/haskel/chapter5/data_transformation.hs`
