# Chapter 9: Immutability & State

## Overview
This chapter explores the profound mathematical truth that "mutability" does not exist. We frame state change not as in-place mutation, but as categorical mappings (morphisms) from one static state object to a new one. This theoretical understanding leads directly to practical implementations of persistent data structures and the functional State Monad pattern.

## Section 1: The Concept of Immutability (A Mathematical Viewpoint)
- **Math has no "time" or "mutation":** Discussing how $x = 5$ means $x$ is 5 perpetually. The concept of $x = x + 1$ implies "time", which is an artifact of computing execution, not a mathematical reality.
- **Categorical Viewpoint:** Objects in a category do not change. To transition state, we use a Morphism to map to a completely new object.
- **Python Analogy:** Immutable types (`tuple`, `frozenset`) vs mutable types (`list`, `dict`), and why functional programming leans heavily into immutability to retain mathematical purity.

## Section 2: Persistent Data Structures
- Creating modified copies rather than in-place changes.
- **Structural Sharing:** The technique functional languages use to make immutable updates memory-efficient and performant without deep-copying entire data sets.
- **Haskell vs. Python:** Demonstrating how Haskell intrinsically uses structural sharing for lists, and conceptually how we can mimic this in Python.

## Section 3: The Categorical View of State
- **Managing State as Functions:** Since we cannot modify variables globally, we transition state by passing it through functions.
- **The State Monad Concept:** Describing a stateful computation as a function $S \to (A \times S)$. It takes an initial state $S$, and returns a pair containing the generated value $A$ and the new state $S'$. This approach threads state identically to mathematical mappings.

## File Structure
- `Contents/text/chapter9_immutability/chapter9_main.tex`
- `Contents/code/python/chapter9/immutability_math.py`
- `Contents/code/python/chapter9/state_monad_concept.py`
- `Contents/code/haskel/chapter9/structural_sharing.hs`
