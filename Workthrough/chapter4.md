# Workthrough Chapter 4: Functions as First-Class Citizens

## Section Breakdown

1. **What Does "First-Class" Mean?**
   - Contrast traditional static functions with functions as data.
   - Three rules of First-Class citizens:
     1. Can be assigned to a variable.
     2. Can be passed as an argument.
     3. Can be returned as a result.

2. **Passing Functions as Data (Code)**
   - Show how to pass an operation (e.g., `add_one` or `multiply_by_two`) into an `apply_twice` function.
   - Python: `Callable[[int], int]` type hints.
   - Haskell: `(Int -> Int)` type signature.

3. **Higher-Order Functions**
   - Definition: A function that takes a function as an argument, or returns one.
   - Analogy to Calculus: The derivative operator $d/dx$ is a HOF.

4. **The Holy Trinity: Map, Filter, and Reduce**
   - **Map:** Applies a function to every item in a container.
   - **Filter:** Keeps items matching a predicate function.
   - **Reduce (Fold):** Combines elements into a single value using an accumulator function.

5. **A Gentle Introduction to Functors**
   - Category Theory link: Objects (Types) and Morphisms (Functions).
   - What if we map between entire categories? -> Functors.
   - Practical view: A Functor is any container/context (like a List) that can be mapped over using a First-Class function.
   - By passing a function into `map`, you are lifting a simple data transformation into a higher mathematical dimension.

## Resources Created
- **Text:** `Contents/text/chapter4_firstclass/chapter4_main.tex`
- **Python:** `Contents/code/python/chapter4/firstclass.py`
- **Haskell:** `Contents/code/haskel/chapter4/firstclass.hs`
