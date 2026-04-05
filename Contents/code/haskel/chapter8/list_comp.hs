module Main where

dataList :: [Int]
dataList = [1..10]

-- List comprehension equivalent to combining map and filter in Python
evenSquares :: [Int]
evenSquares = [x * x | x <- dataList, x `mod` 2 == 0]

-- Example with multiple generators (like a nested loop)
pairs :: [(Int, Int)]
pairs = [(x, y) | x <- [1, 2], y <- [3, 4]]

-- An infinite lazy list comprehension 
-- Taking only the first 3 elements showing lazy evaluation
lazyEvaluated :: [Int]
lazyEvaluated = take 3 [x * x | x <- [1..]]

main :: IO ()
main = do
    putStrLn $ "Even squares: " ++ show evenSquares
    putStrLn $ "All pairs: " ++ show pairs
    putStrLn $ "Lazy evaluated: " ++ show lazyEvaluated
