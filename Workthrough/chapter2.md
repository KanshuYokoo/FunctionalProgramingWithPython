# Workthrough Chapter 2: The Calculus of Functions

## Section Breakdown
1. **Introduction to Lambda Calculus**
   - Alonzo Church and his invention of $\lambda$-calculus vs. Alan Turing's Turing Machine.
   - The three components of Lambda Calculus: Variables, Abstractions ($\lambda$), and Applications.
   - Syntax: $\lambda x . x + 1$
2. **Anonymous Functions in Code**
   - Explain how lambda abstractions map directly to anonymous functions in code.
   - Show Python's `lambda x: x + 1`.
   - Show Haskell's `\x -> x + 1`.
3. **Bound vs. Free Variables**
   - The conceptual difference between defining an input parameter (bound) and relying on the surrounding environment (free).
   - Combinators (e.g., Identity function $\lambda x . x$).
4. **The Rules of Computation**
   - How functional languages evaluate code (unlike Turing machines' state changes).
   - **Alpha-conversion** ($\alpha$-conversion): Renaming bound variables (e.g., $\lambda x . x = \lambda y . y$). Mention namespace collision avoidance.
   - **Beta-reduction** ($\beta$-reduction): The act of function application. Show step-by-step substitution of arguments into the function body.
     - $(\lambda x . x + 1)\ 5 \xrightarrow{\beta} 5 + 1 \rightarrow 6$
5. **Why This Matters**
   - Conclusion bridging theory to practice: all functional programming translates back to an immense tree of beta reductions.

## Resources Created
- **Text:** `Contents/text/chapter2_calculus/chapter2_main.tex`
- **Python:** `Contents/code/python/chapter2/lambdas.py`
- **Haskell:** `Contents/code/haskel/chapter2/lambdas.hs`
