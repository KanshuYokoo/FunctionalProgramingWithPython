-- Input list
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

-- Fold (Reduce) combines the list elements using left fold
totalSum :: Int
totalSum = foldl (+) 0 numbers
-- totalSum == 15

main :: IO ()
main = do
  print squares
  print evens
  print totalSum
