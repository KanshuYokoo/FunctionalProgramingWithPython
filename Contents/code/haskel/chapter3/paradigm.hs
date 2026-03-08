-- Haskell is declarative by nature.
-- There are no for-loops or mutable variables.

-- DECLARATIVE STYLE: Recursive definition of sum.
-- This declares "what" a sum IS, not "how" to compute it.
mySum :: [Int] -> Int
mySum []     = 0              -- base case: the sum of an empty list is 0
mySum (x:xs) = x + mySum xs  -- recursive case: head + sum of the tail

-- Haskell's built-in 'sum' is defined the same way via 'foldr'.
-- sum [1,2,3,4,5] == 15
