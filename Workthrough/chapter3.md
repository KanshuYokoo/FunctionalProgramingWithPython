# Workthrough Chapter 3: The Functional Paradigm

## Section Breakdown

1. **Two Ways to Think About Programs**
   - Contrast imperative (how) vs. declarative (what) style.
   - Imperative: step-by-step mutation of a `total` variable using a for-loop.
   - Declarative: recursive definition expressing the relationship, not the procedure.

2. **Python vs. Haskell contrast (Code)**
   - Python `imperative_sum`: explicit loop with mutable accumulator.
   - Python `functional_sum`: recursive, no mutation.
   - Haskell `mySum`: pattern-matched recursive definition (declarative by enforced design).

3. **Pure Functions**
   - Two rules: deterministic output, no side effects.
   - Category Theory link: a pure function = a genuine morphism (reliable arrow between types).
   - Python comparison: `add(x, y)` (pure) vs. `increment_and_add(x)` (impure—reads/modifies global state).

4. **Side Effects**
   - Definition: any observable interaction beyond returning a value.
   - Examples: print, file I/O, network, global mutation, exceptions.
   - Functional approach: isolate effects to the periphery; keep core logic pure.
   - Haskell's `IO` type enforces this separation at the compiler level.

5. **Referential Transparency**
   - Definition: an expression can be replaced by its value without changing program behaviour.
   - Demonstration: `add(2,3) + add(2,3)` can be replaced by `5 + 5`.
   - `increment_and_add` violates this (result changes each call).
   - Enables equational reasoning: treating code like algebra.
   - Category Theory link: referential transparency is what makes functions true morphisms.

## Resources Created
- **Text:** `Contents/text/chapter3_paradigm/chapter3_main.tex`
- **Python:** `Contents/code/python/chapter3/paradigm.py`
- **Haskell:** `Contents/code/haskel/chapter3/paradigm.hs`
