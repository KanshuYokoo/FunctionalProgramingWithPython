# Workthrough Chapter 1: Introduction to Mathematical Functions

## Section Breakdown
1. **What is a Function?**
   - Simple introduction mapping functions to a reliable machine.
   - The formula $f(x) = y$.
2. **Domains and Codomains**
   - Formal mathematical definition of Sets.
   - Domains (valid inputs) and Codomains (possible outputs).
   - Mapping notation ($f : A \rightarrow B$).
3. **From Mathematics to Code**
   - Contrast standard Python imperative functions with mathematical "pure" functions.
   - Introduce the two rules of a pure function:
     1. Same output for the same input.
     2. No observable side effects.
4. **A Simple Mapping (Python and Haskell Code)**
   - Start with a simple mathematical function: $f(x) = x^2$ over Integers.
   - Show how Python Type Hints (`x: int -> int`) mirror formal sets.
   - Show how Haskell explicitly enforces pure mathematical mappings with its type signatures (`square :: Int -> Int`).
5. **An Early Glimpse at Category Theory**
   - Summarize the previous concepts: Sets, Functions, Arrows.
   - Introduce the foundational components of a Category:
     - Objects (Types/Sets)
     - Morphisms (Functions/Arrows)
   - Conclude that programming with pure functions is simply defining morphisms between objects in the "Category of Types" (or *Hask*).

## Resources Created
- **Text:** `Contents/text/chapter1_introduction/main.tex`
- **Python:** `Contents/code/python/chapter1/functions.py`
- **Haskell:** `Contents/code/haskel/chapter1/functions.hs`
