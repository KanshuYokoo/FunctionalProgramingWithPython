-- A standard named function
addOneNamed :: Int -> Int
addOneNamed x = x + 1

-- The Lambda Calculus equivalent: an anonymous function
-- Syntax: \bound_variable -> body
-- (The backslash '\' looks like a lambda 'lambda')
addOneLambda :: Int -> Int
addOneLambda = \x -> x + 1

-- Beta-reduction in Haskell (Application)
-- (\x -> x + 1) 5
result :: Int
result = (\x -> x + 1) 5
-- result evaluates to 6
