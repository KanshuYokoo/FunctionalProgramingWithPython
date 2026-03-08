-- A simple pure function
addOne :: Int -> Int
addOne x = x + 1

-- HIGHER-ORDER FUNCTION
-- Takes a function (Int -> Int) and an Int, returns an Int
applyTwice :: (Int -> Int) -> Int -> Int
applyTwice f x = f (f x)

-- applyTwice addOne 5   == 7
-- applyTwice (*2) 5     == 20

-- MAP AND FILTER in Haskell

numbers :: [Int]
numbers = [1, 2, 3, 4, 5]

-- Map applies a function to an entire list
squares :: [Int]
squares = map (\x -> x * x) numbers 
-- squares == [1, 4, 9, 16, 25]

-- Filter keeps items matching the predicate
evens :: [Int]
evens = filter (\x -> x `mod` 2 == 0) numbers
-- evens == [2, 4]

-- Fold (Reduce) combines the list elements
totalSum :: Int
totalSum = foldl (+) 0 numbers
-- totalSum == 15
